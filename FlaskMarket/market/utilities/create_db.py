from market import app, db
from market.models import Item, User
# from werkzeug.security import generate_password_hash  # For securely hashing passwords

# List of items to add (example data)
items_data = [
    {"name": "Laptop", "barcode": "123456789012", "price": 999.99,"count": 5, "description": "Macbook Air and Pro"},
    {"name": "Smartphone", "barcode": "987654321098", "price": 699.99,"count": 5, "description": "Latest Android Smartphone"},
    {"name": "Headphones", "barcode": "567890123456", "price": 199.99,"count": 5, "description": "Noise-cancelling headphones"}
]

# List of users to add (example data)
users_data = [
    {"username": "john_doe", "email_address": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email_address": "jane@example.com", "password": "mysecurepassword"},
    {"username": "alice_wonder", "email_address": "alice@example.com", "password": "alicepass"}
]

# Ensure the Flask app runs in the correct application context
with app.app_context():
    db.create_all()  # Create all tables in the database
    print("Database created successfully!")


    # Add items to the database
    for item_data in items_data:
        item = Item(
            name=item_data["name"],
            barcode=item_data["barcode"],
            price=item_data["price"],
            count=item_data["count"],
            description=item_data["description"]
        )
        db.session.add(item)  # Add item to the session

    if not users_data:
        # Add users to the database (with password hashing)
        for user_data in users_data:
            # hashed_password = generate_password_hash(user_data["password"], method='sha256')  # Hash the password securely
            hashed_password = user_data["password"]
            user = User(
                username=user_data["username"],
                email_address=user_data["email_address"],
                password_hash=hashed_password
            )
            db.session.add(user)  # Add user to the session

    db.session.commit()  # Commit the session to save all items and users

    print("Items and users added successfully!")
