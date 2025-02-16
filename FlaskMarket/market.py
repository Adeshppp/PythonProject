from enum import unique

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    # items = [
    #     {"id": 1, "name": "Laptop", "barcode": "123456789012", "price": 999.99},
    #     {"id": 2, "name": "Smartphone", "barcode": "987654321098", "price": 699.99},
    #     {"id": 3, "name": "Headphones", "barcode": "567890123456", "price": 199.99}
    # ]
    items = Item.query.order_by(Item.id).all()
    return render_template("market.html", items = items)