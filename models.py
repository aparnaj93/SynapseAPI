from app import db


class EmployeeInfo(db.Model):
    __tablename__ = 'employee_info'
    emp_id = db.Column('empid', db.Integer, primary_key=True)
    emp_name = db.Column('empname', db.String(200))
    department = db.Column('department', db.String(200))
    address = db.Column('address', db.String(200))
    salary = db.Column('salary', db.Integer)

    def __init__(self, emp_id, emp_name, department, address, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.address = address
        self.salary = salary