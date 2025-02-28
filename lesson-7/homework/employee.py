import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"

class EmployeeManager:
    file_name = 'employees.txt'

    def __init__(self):
        if not os.path.exists(self.file_name):
            # File doesn't exist, so create it  in append mode
            with open(self.file_name, 'a'):
                pass  # Just create the file

    def add(self, employee):
        """Add an employee to the 'employees.txt' file."""
        with open(self.file_name, 'a') as file:  # Open file in append mode to add from where it comes
            file.write(str(employee) +'\n')
    def get_employee_input(self):
        try:
            employee_id=int(input("Enter employee id: "))
            name=input("Enter employee's name: ")
            position=input("Enter employee's position: ")
            salary=int(input("Enter employee's salary: "))
            new_employee=Employee(employee_id,name,position,salary)
            self.add(new_employee)
            print("Employee added succesfully")
        except ValueError:
            print("Invalid error. Make sure you entered true values")
    def view(self):
        """Viewing the file"""
        try:
            with open(self.file_name, 'r') as file:
                f=file.readlines()
                for employee in f:
                    print(employee.strip())
        except FileNotFoundError:
            print("File is not found")
    def search(self):
        """search employee by his/her id"""
        try:
            employee_id=int(input("Enter employee's id you want to search: "))
            with open(self.file_name,'r') as file:
                found=False
                for line in file:
                    parts=line.strip().split(',')
                    if int(parts[0])==employee_id:
                        found=True
                        print(f"employee with employee id {employee_id}: {parts[1]},{parts[2]},{parts[3]}")
                        break
                if not found:    
                    print(f"Employee with {employee_id} is not found")
        except ValueError:
            print("Invalid employee id. Please enter valid employee id")
    def update(self):
        """Updates the information of an employee by their employee ID."""
        employee_id = int(input("Enter employee ID to update: "))
        with open(self.file_name, 'r') as file:
            found = False
            new_employee = []
            for line in file:
                parts = line.strip().split(',')
            # Compare employee ID after converting parts[0] to int
                if int(parts[0]) == employee_id:
                    name = input("Enter new employee name: ")
                    position = input("Enter new employee position: ")
                    salary = int(input("Enter new employee salary: "))
                    updated_employee = Employee(employee_id,name, position, salary)
                    new_employee.append(f"{updated_employee.employee_id},{updated_employee.name},{updated_employee.position},{updated_employee.salary}\n")
                    found = True  # Mark as found
                else:
                    new_employee.append(line)
                
            if found:
                with open(self.file_name, 'w') as file:
                    file.writelines(new_employee)
                print(f"Employee with ID {employee_id} has been updated.")
            else:
                print(f"Employee with ID {employee_id} is not found.")
    def delete(self):
        """Deletes an employee by their employee ID."""
        try:
            employee_id = int(input("Enter employee ID to delete: "))
        
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
        
            found = False
            updated_lines = []  # To store the lines that will remain in the file
        
            for line in lines:
                parts = line.strip().split(',')
                # Compare the employee ID after converting parts[0] to an integer
                if int(parts[0]) == employee_id:
                    found = True
                    print(f"Employee with ID {employee_id} has been deleted.")
                else:
                    # Keep the line if the employee ID doesn't match
                    updated_lines.append(line)
        
            if not found:
                print(f"Employee with ID {employee_id} not found.")
            else:
                with open(self.file_name, 'w') as file:
                    file.writelines(updated_lines)  # Write the updated lines back to the file
                print("Employee data updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid employee ID.")

#asking user to enter the option 
print("Welcome to Employee Records Manager!")
manager=EmployeeManager()
print("1. Add new employee record")
print("2. View all employee records")
print("3. Search for an employee by Employee ID")
print("4. Update an employee's information")
print("5. Delete an employee record")
print("6. Exit")
while True:
    user_info=int(input("Enter your choice: "))
    if user_info==1:
        manager.get_employee_input()
    elif user_info==2:
        manager.view()
    elif user_info==3:
        manager.search()
    elif user_info==4:
        manager.update()
    elif user_info==5:
        manager.delete()
    elif user_info==6:
        print("Good bye")
        break
    else:
        print("Invalid option! Please enter a valid option.")





                        





            



