import sqlite3
from flask_restful import Resource
from flask_restful import reqparse
from flask_jwt import jwt_required
from models.auto import AutoModel


class AutoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('max_speed', type=int, required=True, help='This field cannot be blank')
    parser.add_argument('distance', type=int, required=True, help='This field cannot be blank')
    parser.add_argument('handler', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('stock', type=str, required=True, help='This field cannot be blank')

    @jwt_required()    
    def get(self, mark):
        auto = AutoModel.search_mark(mark)
        if not auto:
            return {'error': 'Auto with that mark not found'}, 404
        return {'auto': auto}, 200

    @jwt_required()
    def post(self, mark):
        auto = AutoModel.search_mark(mark)
        if auto:
            return {'error': 'Auto with that mark exists'}, 400
        data = AutoResource.parser.parse_args()
        auto = AutoModel(mark, data['max_speed'], data['distance'], data['handler'], data['stock'])
        auto.insert()

        return {'message': 'Auto created'}, 201

    @jwt_required()
    def put(self, mark):
        auto = AutoModel.search_mark(mark)
        if not auto:
            return {'error': 'Auto with that mark not found'}, 404
        data = AutoResource.parser.parse_args()
        auto = AutoModel(data['max_speed'], data['distance'], data['handler'], data['stock'], mark)
        auto.update()
        return {'message': 'Auto updated'}, 202

    @jwt_required()
    def delete(self, mark):
        auto = AutoModel.search_mark(mark)
        if not auto:
            return {'error': 'Auto with that mark not found'}, 404
        auto = AutoModel(mark, None, None, None, None)
        auto.delete()
        return {'message': 'Auto deleted'}, 202
