from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, email = {email}, department = {department}, salary = {salary})"

db.create_all( )

employee_put_args = reqparse.RequestParser()
employee_put_args.add_argument("id", type=int, help="Please fill in your id number.", required=True)
employee_put_args.add_argument("name", type=str, help="Please fill in your name.", required=True)
employee_put_args.add_argument("email", type=str, help="Please fill in your email address.", required=True)
employee_put_args.add_argument("department", type=str, help="Please fill in the name of department.", required=True)
employee_put_args.add_argument("salary", type=float, help="Please fill in the salary.", required=True)
#employee_put_args.add_argument("birth_date", type=int, help="Please fill in the birth date.", required=True)

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