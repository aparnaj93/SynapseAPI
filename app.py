from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import models
import json
import serializers

app = Flask(__name__)
POSTGRES = {
    'user': 'osuazacn',
    'pw': '2h6fbdeZ54BuNl39UcWW5EMEOyCzRRBd',
    'db': 'osuazacn',
    'host': 'baasu.db.elephantsql.com',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:%s/%s' % (POSTGRES['user'], POSTGRES['pw'],
                                                                         POSTGRES['host'], POSTGRES['port'],
                                                                      POSTGRES['db'])
db = SQLAlchemy(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/employees/', methods=['POST', 'GET'])
def employee_list_or_create():
    if request.method == "POST":
        try:
            post_data = json.loads(request.data)
            # Create an EmployeeInfo object from POST data
            employee = models.EmployeeInfo(post_data["emp_id"], post_data["emp_name"], post_data["department"],
                                           post_data["address"], post_data["salary"])
            db.session.add(employee)
            db.session.commit()
            return jsonify({"message": "Employee added to database"})
        except Exception as ex:
            db.session.rollback()
            return "Error while inserting new employee: %s" % ex.message
    elif request.method == "GET":
        try:
            employees = models.EmployeeInfo.query.all()
            # Serialize from EmployeeInfo object to JSON
            json_employees = serializers.EmployeeInfoSerializer(employees).to_json()
            return jsonify(json_employees)
        except Exception as ex:
            db.session.rollback()
            return "Error while fetching employee list: %s" % ex.message


@app.route('/employees/<int:id>/', methods=['GET', 'DELETE'])
def get_employee(id):
    if request.method == "GET":
        try:
            # Get employee by ID
            employee = models.EmployeeInfo.query.get(id)
            # Serialize from EmployeeInfo object to JSON
            json_employee = serializers.EmployeeInfoSerializer([employee]).to_json()
            return jsonify(json_employee)
        except Exception as ex:
            return "Error while fetching employee : %s" % ex.message
    elif request.method == "DELETE":
        try:
            # Get employee by ID
            employee = models.EmployeeInfo.query.get(id)
            db.session.delete(employee)
            db.session.commit()
            return jsonify({"message": "Employee deleted from database"})
        except Exception as ex:
            return "Error while deleting employee list: %s" % ex.message


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
