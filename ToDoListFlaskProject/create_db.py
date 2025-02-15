from app import db, app

# Ensure the Flask app runs in the correct application context
with app.app_context():
    db.create_all()
    print("Database created successfully!")
