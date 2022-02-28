from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

names = {'olawale': {'age': 25, 'location': 'Lagos'},
        'kalipha': {'age': 22, 'location': 'Ibafo'},
         }


class HelloWorld(Resource):
    def get(self, name,):
        return names[name]


class Base(Resource):
    def get(self):
        return {'data': 'Welcome User'}


api.add_resource(Base, '/')
api.add_resource(HelloWorld, '/hello/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
