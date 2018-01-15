class Employee:
    # Common base class for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @classmethod
    def display_count(cls):
        # "class name : Employee"
        print(f"Total Employee { Employee.empCount }")

    def display_employee(self):
        print("Name : " + self.name + f", Salary: { self.salary } ")


# This would create first object of Employee class
EMP1 = Employee("Zara", 2000)
# This would create second object of Employee class"
EMP2 = Employee("Manni", 5000)
EMP1.display_employee()
EMP2.display_employee()
print(f"Total Employee  { Employee.empCount } ")
