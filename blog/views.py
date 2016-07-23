from flask import render_template, redirect, url_for, request, session,flash
from blog import app
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from blog.models import User
from blog import db

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

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/register",methods = ('GET','POST'))
def register():
    form = Register()
    if request.method == 'POST'  and form.validate():
        new_user = User(request.form['name'],request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        session['username'] = request.form['name']
        flash('You created a new user')
        return redirect(url_for('index'))
    return render_template('register.html',form = form)

@app.route("/login",methods = ('GET','POST'))
def login():
    form = LogIn()
    if request.method == 'POST'  and form.validate():
        user = User.query.filter_by(username= request.form['name']).first()
        if user != None:
            user.check_password(request.form['password'])
            session['username'] = request.form['name']
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login')
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were successfully logged out')
    return redirect(url_for('index'))
