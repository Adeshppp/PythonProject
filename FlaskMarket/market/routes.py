from market import app
from flask import Flask, render_template

from market.models import Item


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    items = Item.query.order_by(Item.id).all()
    return render_template("market.html", items = items)