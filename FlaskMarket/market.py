from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    items = [
        {"id": 1, "name": "Laptop", "barcode": "123456789012", "price": 999.99},
        {"id": 2, "name": "Smartphone", "barcode": "987654321098", "price": 699.99},
        {"id": 3, "name": "Headphones", "barcode": "567890123456", "price": 199.99}
    ]
    return render_template("market.html", items = items)