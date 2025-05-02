class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee 

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        print("Employee Info:", self.employee.get_details())

emp1 = Employee("Alice", 101)

dept1 = Department("HR", emp1)

dept1.show_department_info()
