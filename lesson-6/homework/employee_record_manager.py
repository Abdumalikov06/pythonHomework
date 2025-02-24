def employees():
    with open('employees.txt', 'a') as file:
        employee_id = int(input("Enter Employee ID: "))
        employee_name = input("Enter employee name: ").title()
        employee_position = input("Enter employee position: ").title()
        employee_salary = int(input("Enter employee salary: "))
        employee_records = f"{employee_id},{employee_name},{employee_position},{employee_salary}\n"
        file.write(employee_records)
def search_by_employeeid(employee_id):
    with open('employees.txt','r') as file:
        found = False
        for line in file:
            if line.startswith(str(employee_id)):
                print("Employee found:",line.strip())
                found=True
                break
    if not found:   
        print(f"employee with {employee_id} is not found")
def update_employee(employee_id):
    employees=[]
    found=False
    with open('employees.txt', 'r') as file:
        for line in file:
            if line.startswith(str(employee_id)):
                print("Employee is found:", line.strip())
                name=input("Enter a new name:").title()
                position=input("Enter a position: ").title()
                salary=int(input("Enter salary: "))
                updated_records=f"{employee_id},{name},{position},{salary}\n"
                employees.append(updated_records)
                found=True
            else:
                employees.append(line)
    if found:
        with open('employees.txt', 'w') as f:
            f.writelines(employees)
        print("employee updated successfully")
    else:
        print(f"employee with {employee_id} is not found")
def employee_delete_record(employee_id):
    found=False
    employees=[]
    with open('employees.txt','r') as file:
        for line in file:
            if line.startswith(str(employee_id)):
                found=True
                print(f"Employee with {employee_id} is deleted")
            else:
                employees.append(line)
    if found:
        with open('employees.txt','w') as file:
            file.writelines(employees)
    else:
        print(f"Employee with {employee_id} is not found")

                    
while True:
    print("MENU OPTIONS:")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    user_information=int(input("Enter an option number: "))
    if user_information==1:
        employees()
    elif user_information==2:
        with open('employees.txt','r') as file:
            info=file.read()
            if info:
                print(info)
            else:
                print("no employee records found")
    elif user_information==3:
        input_empl_id=int(input("Enter employee id: "))
        search_by_employeeid(input_empl_id)
    elif user_information==4:
        user_info_for_update=int(input("Enter the employee id you want to update: "))
        update_employee(user_info_for_update)
    elif user_information==5:
        user_info_for_delete=int(input("Enter employee id you want to delete: "))
        employee_delete_record(user_info_for_delete)
    elif user_information==6:
        print("Exiting...")
        break
    else:
        print("You entered wrong option")


       



