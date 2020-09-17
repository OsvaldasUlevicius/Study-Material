from user import User
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password): # safe str cmp works on all python versions and systems, its safer to compare strings
        return user

def identity(payload): # payload is the content of JWT token
    user_id = payload['identity']
    return User.find_by_id(user_id)
