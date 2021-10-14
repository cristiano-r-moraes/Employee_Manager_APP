from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import os


#Configurations setup
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


#Declaration of the Tables for the database
class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Employee(name = {self.name}, email = {self.views}, department = {self.likes}, salary = {self.salary})"

class ReportsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Reports(name = {self.name}, email = {self.views}, department = {self.likes}, salary = {self.salary})"


employee_put_args = reqparse.RequestParser()
employee_put_args.add_argument("name", type=str, help="Please fill in your name.", required=True)
employee_put_args.add_argument("email", type=str, help="Please fill in your email address.", required=True)
employee_put_args.add_argument("department", type=str, help="Please fill in the name of department.", required=True)
employee_put_args.add_argument("salary", type=float, help="Please fill in the salary.", required=True)

employee_update_args = reqparse.RequestParser()
employee_update_args.add_argument("name", type=str, help="Please fill in your name.")
employee_update_args.add_argument("email", type=str, help="Please fill in your email address.")
employee_update_args.add_argument("department", type=str, help="Please fill in the name of department.")
employee_update_args.add_argument("salary", type=float, help="Please fill in the salary.")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'department': fields.String,
    'salary': fields.Float
}


#get the values from the environment variables 
Admin_key = os.environ['admin_key']
Password_key = os.environ['password']

USER_DATA = {
    Admin_key : Password_key     
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class Employees(Resource):

    @auth.login_required #authentication required -> added in all methods
    @marshal_with(resource_fields) #this decorator is meant to make the EmployeesModel object serializable
    def get(self, employee_id=None):
        if employee_id:              
            result = EmployeeModel.query.filter_by(id=employee_id).first()
            if not result:
                abort(404, message="Could not find employee with this id")
            return result
        else:
            result = EmployeeModel.query.all()
            if not result:
                abort(404, message="Could not find employee with this id")
            return result
        
    @auth.login_required    
    @marshal_with(resource_fields)
    def put(self, employee_id): 
        args = employee_put_args.parse_args()
        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if result:
            abort(409, message="Employee id taken...")
        
        employee = EmployeeModel(id=employee_id, name=args['name'], email=args['email'], department=args['department'], salary=args['salary']) 
        db.session.add(employee)
        db.session.commit()
        return employee, 201 #201 - added the employee successfully

    @auth.login_required
    @marshal_with(resource_fields)
    def patch(self, employee_id):
        args = employee_update_args.parse_args()
        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['email']:
            result.email = args['email']
        if args['department']:
            result.department = args['department']
        if args['salary']:
            result.salary = args['salary']
        
        db.session.commit()

        return result
    
    @auth.login_required
    @marshal_with(resource_fields)
    def delete(self, employee_id):
        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if not result:
            abort(404) #Could not find employee with this id
        db.session.delete(result)
        db.session.commit()
        return '', 204 #204 - deleted successfully        


class Reports(Resource):

    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, type):
        if type == 'age':
            result = ReportsModel.query.all()            
            return result

#Rotes setup
api.add_resource(Employees, "/employees/<int:employee_id>", "/employees/")
api.add_resource(Reports, "/reports/employees/<string:type>/" )


if __name__ == "__main__":
    app.run(debug=True)