from db import db

class ItemModel(db.Model): # tells sqlalchemy entity that these classes/models are things that we are going to be saving and retrieving from the database
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True) # id will be created, but since there is no id in init function, it will not be used
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # into the foreign key goes tablename.columnname
    store = db.relationship('StoreModel') # similar to join in sql / the sqlalchemy sees the previous variable (store_id) and on this line it can find it
    # now every item model has a store which is a store that matches the store_id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): # returns a json representation of the model
        return {'name': self.name, 'price': self.price}

    @classmethod # this is a class method because it returns an object of ItemModel as opposed to dictionary
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self) # a collection of objects that we are going to write into the database / INSERT INTO / also updates because ids are unique
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
