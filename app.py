from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class employees(Resource):
    def get(self):
        return
    
    def put(self):
        return
    
    def delete(self):
        return

api.add_resource(employees, "")

if __name__ == "__main__":
    app.run(debug=True)