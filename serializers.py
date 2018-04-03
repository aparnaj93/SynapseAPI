class EmployeeInfoSerializer:
    def __init__(self, employees):
        self.employees = employees

    def to_json(self):
        resp = []
        for employee in self.employees:
            resp.append(
                {
                    "EmployeeID": employee.emp_id,
                    "EmployeeName": employee.emp_name,
                    "Department": employee.department,
                    "Address": employee.address,
                    "Salary": employee.salary
                }
            )
        return resp
