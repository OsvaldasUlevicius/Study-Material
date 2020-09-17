from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # backreference - allows the store to see which items are in the items table with a store id equal to its own id
    items = db.relationship('ItemModel', lazy='dynamic') # a list of item models - a many (items) to one (store) relationship
    # lazy='dynamic' whenever there is created a new store, the program automaticaly creates a new object for each item - lazy turns this off

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
