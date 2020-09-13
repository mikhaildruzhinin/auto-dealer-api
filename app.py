from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from secure.auth_conf import authenticate, identity
from resources.register import RegisterResource
from resources.auto import AutoResource
# from resources.stock import StockResource

app = Flask(__name__)
app.secret_key = "MySuperDuperSecretKey"
api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

@app.route('/', methods=['GET'])
def get_root_page():
    return {'msg': 'hello world'}

api.add_resource(AutoResource, '/auto/<string:mark>')
# api.add_resource(StockResource, '/stock')
api.add_resource(RegisterResource, '/register')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
