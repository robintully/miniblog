from blog import app
from blog import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(160))


    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self,password):
        self.pw_hash= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.pw_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username
