from flask import current_app
from blog import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from blog import db
# Creates all models for the SQLAlchemy database and sets configurations

# Users have a name a hashed password
# Users have many posts and have many comments
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(160))
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self,password):
        self.pw_hash= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.pw_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username

# Posts have content, a title, a timestamp, belong to a user, and have many comments
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    title = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='posts')


    def __init__(self, user, title, content):
        self.user_id = user.id
        self.content = content
        self.title = title

    def __repr__(self):
        return '<Post %r>' % self.title

    def format_time(self):
        return str(self.timestamp.month) + "/"+  str(self.timestamp.day) + "/" + str(self.timestamp.year)

# Comments have a content a a timestamp, they belong to both a user and a post
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', backref='comments')


    def __init__(self, user,post, content):
        self.user_id = user.id
        self.post_id = post.id
        self.content = content

    def __repr__(self):
        return '<Comment %r' % self.content

   
