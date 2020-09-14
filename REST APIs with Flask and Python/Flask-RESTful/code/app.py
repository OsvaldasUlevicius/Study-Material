from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates a new endpoint /auth | when we call /auth we send it an username and password
# JWT extension sends that information to the authenticate function and then we get returned a jwt token(an user)
# next we will send the jwt token and the jwt is going to call the identity function, which gets the user id and gets the correct
# user for that user_id that the jwt token represents

items = []

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}

class Item(Resource):
       parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be left blank!'
        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) # filter function returns a filter object/ next - gives us the first item found by filter function / if the next object does not find an item it will return None
        #for item in items: # A longer way of doing this
            #if item['name'] == name:
                #return item
        #return {'message': 'Item does not exist!'}
        #return {'item': None}, 404
        return {'item': item}, 200 if item else 404

    def post(self, name): # POST has to have the same parameters as GET
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with the name \'{}\' already exists'.format(name)}, 400
        #data = request.get_json() # force=True parametras - means that you don't need content-type header, it will look at the content and format it accordingly to json/ silent=True returns none ------ ways to react if we receive not json
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items)) # create a new items list not containing the one item, that i want to delete and override the original items list
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data}
            items.append(item)
        else:
            item.update(data) # dictionaries have an update method
        return item # return the item to reflect that the changes have happened


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)
