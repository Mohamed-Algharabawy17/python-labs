from pymongo import MongoClient


class Employee:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["employee_db"]
    collection = db["employees"]

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        self.insert_into_db()

    def insert_into_db(self):
        employee_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }
        self.collection.insert_one(employee_data)

    def transfer(self, new_department):
        query = {"first_name": self.first_name, "last_name": self.last_name}
        new_values = {"$set": {"department": new_department}}

        result = self.collection.update_one(query, new_values)

        if result.modified_count == 1:
            print("Employee's department has been successfully updated.")
            self.department = new_department
        else:
            print("Failed to update employee's department.")

    def fire(self):
        query = {"first_name": self.first_name, "last_name": self.last_name}
        self.collection.delete_one(query)

    def show(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @classmethod
    def list_employees(cls):
        employees = cls.collection.find()
        for emp in employees:
            print(
                f"First Name: {emp['first_name']}, Last Name: {emp['last_name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")


class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("Salary: Confidential")
        print(f"Managed Department: {self.managed_department}")


def interface_menu():
    while True:
        print("\nMenu:")
        print("1. Add a new employee (enter 'add')")
        print("2. Transfer an employee (enter 'transfer')")
        print("3. Fire an employee (enter 'fire')")
        print("4. List all employees (enter 'list')")
        print("5. Exit the program (enter 'q')")

        command = input("\nEnter your choice: ").strip().lower()

        if command == "add":
            role = input("If manager press 'm', if employee press 'e': ").strip().lower()
            if role == 'e':
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                Employee(first_name, last_name, age, department, salary)
                print("Employee added successfully!")
            elif role == 'm':
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                managed_department = input("Managed Department: ")
                Manager(first_name, last_name, age, department, salary, managed_department)
                print("Manager added successfully!")
            else:
                print("Invalid input. Please try again.")
        elif command == "transfer":
            first_name = input("First Name of the employee to transfer: ")
            last_name = input("Last Name of the employee to transfer: ")
            new_department = input("New Department: ")
            employee = Employee.collection.find_one({"first_name": first_name, "last_name": last_name})
            if employee:
                emp = Employee(employee["first_name"], employee["last_name"], employee["age"], employee["department"],
                               employee["salary"])
                emp.transfer(new_department)
                print("Employee transferred successfully!")
            else:
                print("Employee not found.")
        elif command == "fire":
            first_name = input("First Name of the employee to fire: ")
            last_name = input("Last Name of the employee to fire: ")
            query = {"first_name": first_name, "last_name": last_name}
            result = Employee.collection.delete_one(query)
            if result.deleted_count == 1:
                print("Employee fired successfully!")
            else:
                print("Employee not found.")
        elif command == "list":
            Employee.list_employees()
        elif command == "q":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


interface_menu()
