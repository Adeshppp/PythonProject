from market import app, db, Item

# List of items from market.py
items_data = [
    {"name": "Laptop", "barcode": "123456789012", "price": 999.99, "description": "Macbook air and pro"},
    {"name": "Smartphone", "barcode": "987654321098", "price": 699.99, "description": "Latest model with 5G support"},
    {"name": "Headphones", "barcode": "567890123456", "price": 199.99, "description": "Noise-cancelling headphones"}
]

# Ensure the Flask app runs in the correct application context
with app.app_context():
    db.create_all()  # Ensure tables are created
    print("Database created successfully!")

    # Add each item to the database
    for item_data in items_data:
        item = Item(
            name=item_data["name"],
            barcode=item_data["barcode"],
            price=item_data["price"],
            description=item_data["description"]
        )
        db.session.add(item)  # Add item to the session
    db.session.commit()  # Commit the session to save the items

    print("Items added successfully!")
