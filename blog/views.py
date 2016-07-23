from blog import app
from flask import render_template, redirect, url_for, request, session
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from blog.models import User

class LogIn(Form):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login",methods = ('GET','POST'))
def login():
    form = LogIn()
    if request.method == 'POST':
        if User.query.filter_by(username= request.form['name']).first().check_password(request.form['password']):
             session['username'] = request.form['name']
             return redirect(url_for('index'))
    return render_template('login.html',form = form)
