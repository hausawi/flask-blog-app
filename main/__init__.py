from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets



app = Flask(__name__)
app.config['SECRET_KEY']= secrets
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from main import routes