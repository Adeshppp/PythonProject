from enum import unique

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)



from market import routes
# from market import create_db