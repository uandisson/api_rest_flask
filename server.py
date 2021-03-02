from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return jsonify({'message':'Hello World!'})

api.add_resource(Users, '/users') 

if __name__ == '__main__':
    app.run()