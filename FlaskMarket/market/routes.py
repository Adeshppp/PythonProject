from crypt import methods

from market import app
from flask import Flask, render_template, redirect, url_for, request,flash
from market.forms import RegisterForm
from market.models import Item, User
from market import db


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    items = Item.query.order_by(Item.id).all()
    return render_template("market.html", items = items)


@app.route('/register', methods=['GET','POST'])
def register_page():
    print("calling register_page")

    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address = form.email_address.data,
            password_hash=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            # flash(f'There was an error while creating a user :{err_msg}', category = "danger")
            flash(err_msg[0], category = "danger")
            print(f'There was an error while creating a user :{err_msg}')
    return render_template('register.html', form = form)


