from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "I need to finish soon"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kyle:pass@localhost/Wishlist'
db = SQLAlchemy(app)

from app import views, model