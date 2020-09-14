from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# we do this so we wouldn't have to iterate over our list every time, instead we use mapping dictionaries to call out the needed
# keys : username_mapping['bob'] / userid_mapping[1]

def authenticate(username, password):
    user = username_mapping.get(username, None) # .get is another way of accessing the dictionary / None - default value
    if user and safe_str_cmp(user.password, password): # safe str cmp works on all python versions and systems, its safer to compare strings
        return user

def identity(payload): # payload is the content of JWT token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
