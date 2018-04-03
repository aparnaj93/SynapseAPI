SETUP:
1. Build a docker image using the following command:
docker build -t flaskapp:latest .

2. Run the docker image using the following command:
docker run -p 5000:5000 flaskapp



Endpoints Supported:
1. GET /employees
Eg: curl -X GET http://0.0.0.0:5000/employees/

2. GET /employees/<id>
Eg: curl -X GET http://0.0.0.0:5000/employees/100/

3. POST /employees
Eg: curl -H "Content-type: application/json" -X POST http://0.0.0.0:5000/employees/ -d '{"emp_id": 102,"emp_name": "Monkey", "address": "New York", "department": "Zoo", "salary": 75000}'



