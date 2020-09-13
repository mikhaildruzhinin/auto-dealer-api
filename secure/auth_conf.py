from models.register import RegisterModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = RegisterModel.search_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    uid = payload['identity']
    return RegisterModel.search_id(uid)