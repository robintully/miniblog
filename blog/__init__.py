from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'super secret key'
app.config['WTF_CSRF_SECRET_KEY'] = 'a random string'
db = SQLAlchemy(app)
Bootstrap(app)
import blog.views


# This is where everything went

# Launch the App
if __name__ == "__main__":
    app.run()
