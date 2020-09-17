from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates a new endpoint /auth | when we call /auth we send it an username and password
# JWT extension sends that information to the authenticate function and then we get returned a jwt token(an user)
# next we will send the jwt token and the jwt is going to call the identity function, which gets the user id and gets the correct
# user for that user_id that the jwt token represents


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
