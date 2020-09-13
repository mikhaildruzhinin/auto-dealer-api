import sqlite3
from flask_restful import Resource, reqparse
from models.register import RegisterModel

# Пользовательский ресурс
class RegisterResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username field required')
    parser.add_argument('password', type=str, required=True, help='Password field required')
    
    def post(self):
        request_body = RegisterResource.parser.parse_args()
        if RegisterModel.search_username(request_body['username']):
            return {'error': 'User already exists'}, 400

        user = RegisterModel(None, request_body['username'], request_body['password'])
        user.insert()

        return {'message': 'User created. Try to auth'}, 201
