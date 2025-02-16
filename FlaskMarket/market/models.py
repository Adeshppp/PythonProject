
from market import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name