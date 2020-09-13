import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required
from models.auto import AutoModel


class Stock(Resource):
    @jwt_required()    
    def get(self):
        cars = AutoModel.get_all()
        if not cars:
            return {'error': 'No one autos found in DataBase'}, 400
        return {'cars': cars}, 200
