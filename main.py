#from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

employee_put_args = reqparse.RequestParser()
employee_put_args.add_argument("id", type=int, help="Please fill in your id number.", required=True)
employee_put_args.add_argument("name", type=str, help="Please fill in your name.", required=True)
employee_put_args.add_argument("email", type=str, help="Please fill in your email address.", required=True)
employee_put_args.add_argument("department", type=str, help="Please fill in the name of department.", required=True)
employee_put_args.add_argument("salary", type=float, help="Please fill in the salary.", required=True)
#employee_put_args.add_argument("birth_date", type=datetime, help="Please fill in the birth date.", required=True)

employees = {}

def if_employee_doesnt_exist(employee_id):
    if employee_id not in employees:
        abort(404, message="Employee ID is not valid!")

def if_employee_exists(employee_id):
    if employee_id in employees:
        abort(409, message="Employee already exists with that ID!")

class Employees(Resource):
    def get(self, employee_id):
        if_employee_doesnt_exist(employee_id)
        return employees[employee_id]
    
    def put(self, employee_id): #function to add a new employee
        if_employee_exists(employee_id)
        args = employee_put_args.parse_args()
        employees[employee_id] = args
        return employees[employee_id], 201 #201 - added the employee successfully
    
    def delete(self, employee_id):
        if_employee_doesnt_exist(employee_id) #if the employee does not exist
        del employees[employee_id]
        return '', 204 #204 - deleted successfully

api.add_resource(Employees, "/employee/<int:employee_id>")

if __name__ == "__main__":
    app.run(debug=True)