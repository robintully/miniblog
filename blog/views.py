from flask import render_template, redirect, url_for, request, session,flash
from blog import app
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from blog.models import User, Post, Comment
from blog import db
from functools import wraps

def user_exists(form,field):
    if User.query.filter_by(username= request.form['name']).first():
        raise ValidationError("name taken")

class LogIn(Form):
    name = StringField('name', validators=[DataRequired('please enter name')])
    password = PasswordField('password', validators=[DataRequired('please enter password')])

class Register(Form):
    name = StringField('name', validators=[DataRequired('please enter name'),user_exists])
    password = PasswordField('password', validators=[DataRequired('please enter password'),EqualTo('confirm_password', message = "passwords must match") ,])
    confirm_password = PasswordField('confirm password', validators=[DataRequired('please enter password')])

class CreatePost(Form):
    title = StringField('title', validators=[DataRequired('please enter title')])
    content = TextAreaField('content', validators=[DataRequired('please enter content')])

class CreateComment(Form):
    content = TextField('content', validators=[DataRequired('please enter content')])

class UpdateForm(Form):
    title = StringField('title', validators=[DataRequired('please enter title')])
    content = TextAreaField('content', validators=[DataRequired('please enter content')])




# @app.context_processor:
# def inject_user():
#     return dict(user= User.query.get(session['user_id'])




# Main Route

@app.route("/")
@app.route("/index")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts = posts)

# Routes for Login and Authentication
@app.route("/register",methods = ('GET','POST'))
def register():
    form = Register()
    if request.method == 'POST'  and form.validate():
        new_user = User(request.form['name'],request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('You created a new user')
        return redirect(url_for('index'))
    return render_template('register.html',form = form)

@app.route("/login",methods = ('GET','POST'))
def login():
    form = LogIn()
    if request.method == 'POST'  and form.validate():
        user = User.query.filter_by(username= request.form['name']).first()
        if user.check_password(request.form['password']):
            session['user_id'] = user.id
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login')
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were successfully logged out')
    return redirect(url_for('index'))

# Admin Route
@app.route('/admin')
def admin():
    if User.query.get(session['user_id']).username == 'admin':
        users = User.query.all()
        posts = Post.query.all()
        comments = Comment.query.all()
        return render_template('admin.html', users = users, posts = posts, comments = comments)



# Post routes

@app.route('/createpost', methods = ('GET','POST'))
def createpost():
    form= CreatePost()
    if request.method == 'POST'  and form.validate() and session['user_id']:
        user = User.query.get(session['user_id'])
        post = Post(user,request.form['title'],request.form['content'])
        db.session.add(post)
        db.session.commit()
        flash('New Post Created')
        return redirect(url_for('show_post',post_id = post.id))
    return render_template('create_post.html', form = form)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('show_user.html', user = user)

# Deletes

@app.route('/delete_post', methods = ['POST'])
def delete_post():
    user = User.query.filter_by(username= session['username']).first()
    post = Post.query.get(request.form['post'])
    for comment in post.comments:
        db.session.delete(comment)
    db.session.delete(post)
    db.session.commit()
    if user.admin:
        return redirect(url_for('admin'))
    return render_template('show_user.html', user = user)

@app.route('/delete_comment', methods = ['POST'])
def delete_comment():
    user = User.query.filter_by(username= session['username']).first()
    comment = Comment.query.get(request.form['comment'])
    db.session.delete(comment)
    db.session.commit()
    if user.admin:
        return redirect(url_for('admin'))
    return render_template('show_user.html', user = user)

@app.route('/delete_user', methods = ['POST'])
def delete_user():
    user = User.query.get(request.form['user'])
    for post in user.posts:
        db.session.delete(post)
    for comment in user.comments:
         db.session.delete(comment)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin'))

# Update
@app.route('/update/<int:post_id>', methods = ['POST'])
def update_post(post_id):

    post = Post.query.get(post_id)
    if request.form['title']:
        post.title = request.form['title'] 
    if request.form['content']:
        post.content = request.form['content']
    db.session.commit()
    return redirect(url_for('show_post',post_id = post.id))




@app.route('/posts/<int:post_id>', methods = ('GET','POST'))
def show_post(post_id):
    post = Post.query.get(post_id)
    form = CreateComment()
    update_form = UpdateForm()
    update_form.title.data = post.title
    update_form.content.data = post.content

    if request.method == 'POST'  and form.validate() and session['username']:
        user = User.query.filter_by(username= session['username']).first()
        comment = Comment(user,post,request.form['content'])
        db.session.add(comment)
        db.session.commit()
        flash('Added Comment')
    return render_template('show_post.html', post = post, form = form, update_form = update_form)