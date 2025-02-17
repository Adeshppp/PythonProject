Install below packages:

    pip install flask
    pip install flask-sqlalchemy
    pip install flask-wtf
    pip install wtforms
    pip install email_validator



set application to run by using flask:

    export FLASK_APP=market.py
    flask run


Enable debug mode:

    export FLASK_DEBUG=1


Dynamic route:

    @app.route("/about/<username>")
    def about_page(username):
        return f"<h1>This is About page of {username}</h1>"

