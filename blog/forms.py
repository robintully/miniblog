from blog import app
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from blog.models import User, Post, Comment
from flask import request

# Each one of these forms is an instance of te WTForms form class, userside validations for the forms are created here, these forms are instantiated in views.py
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
