from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# says that the sqlalchemy database is at the root folder of our project / it doesnt have to be sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # doesnt track every change made, SQLALCHEMy has its own modification tracker that is always used
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request #will run the method before the first request in this app / will create the tables unless they exist already
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # creates a new endpoint /auth | when we call /auth we send it an username and password
# JWT extension sends that information to the authenticate function and then we get returned a jwt token(an user)
# next we will send the jwt token and the jwt is going to call the identity function, which gets the user id and gets the correct
# user for that user_id that the jwt token represents


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
