import os
from enum import unique

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'da43186e7ea7c81f373b635f'
# app.config['SECRET_KEY'] = os.urandom(12).hex()
bcrypt = Bcrypt(app)
from market import routes
# from market import create_db