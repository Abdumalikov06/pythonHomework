import os

class App_details:
    def __init__(self,task_id,title,description,due_date,status):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date if due_date else None
        self.status=status
        
    
    def __str__(self):
        return f"{self.task_id},{self.title},{self.title},{self.description},{self.due_date},{self.status}"
    
class AppManager:
    file_name='todoapp.txt'
    def __init__(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name,'a') as file:
                pass #opens the file if it is not exists
    def add(self,new_task):
        with open(self.file_name,'a') as file:
            file.writelines(str(new_task) +'\n')
    def new_tasks(self):
        try:
            task_id=int(input("Enter task id: "))
            title=input("Enter the title of the task: ")
            description=input("Give description to the task: ")
            due_date=input("Enter due-date (YYYY-MM-DD):")
            status=input("Enter status(e.g: Pending, In Progress, Completed): ")
            new_task=App_details(task_id,title,description,due_date,status)
            self.add(new_task)
            print("new task added successfully!")
        except ValueError:
            print("INvlaid input. try again")
    def view(self):
        """viewing the all information"""
        try:
            with open(self.file_name, 'r') as file:
                f=file.readlines()
                for info in f:
                    print(info.strip())
        except FileNotFoundError:
            print("file is not found") 
    def update(self):
        try:
            upd_id=int(input("Enter task id to search: "))
            with open(self.file_name,'r') as file:
                new_task=[]
                found=False
                for line in file:
                    parts=line.strip().split(',')
                    if int(parts[0])==upd_id:
                        task_id=input("Enter updated id of the task: ")
                        title=input("Enter the title of the task: ")
                        description=input("Give description to the task: ")
                        due_date=input("Enter due-date:")
                        status=input("Enter status(e.g: Pending, In Progress, Completed): ")
                        updated_task=App_details(task_id,title,description,due_date,status)
                        new_task.append(f"{updated_task.task_id},{updated_task.title},{updated_task.description},{updated_task.due_date},{updated_task.status}\n")
                        found=True
                    else:
                        new_task.append(line)
            if found:
                with open(self.file_name, 'w') as file:
                    file.writelines(new_task)
                print(f"Employee with ID {upd_id} has been updated.")
            else:
                print(f"Employee with ID {upd_id} is not found.")
        except ValueError:
            print("Input error, please enter valid input")
    def delete(self):
            del_id=int(input("Enter task id to delete: "))
            
            with open(self.file_name, 'r') as file:
                found=False
                new_task=[]
                f=file.readlines()
                for line in f:
                    part=line.strip().split(',')
                    if int(part[0])==del_id:
                        found=True
                        print(f"task with {del_id} is deleted successfully!")
                    else:
                        new_task.append(line)
            if found:
                with open(self.file_name,'w') as file:
                    file.writelines(new_task)
                    
            else:
                print(f"task with {del_id} is not found")
    def filter(self):
        status_filter = input("Enter the status to filter tasks by (e.g., Pending, In Progress, Completed): ").strip()

        with open(self.file_name, 'r') as file:
            found = False
            f = file.readlines()

        
            for line in f:
                parts = line.strip().split(',')  
                if parts[4].strip().lower() == status_filter.lower():  # Compare status (assumed to be the 5th field)
                    found = True
                    print(f"{parts[0]},{parts[1]},{parts[2]},{parts[3]},{parts[4]}")

        if not found:
            print(f"No tasks found with the status '{status_filter}'.")
    def save(self):
        print("Tasks have been saved successfully!")

    def Load(self):
        """Load all tasks from the file into memory."""
        self.tasks=[]
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) == 5:  # Ensure the line is properly formatted
                        task_id = int(parts[0])
                        title = parts[1]
                        description = parts[2]
                        due_date = parts[3] if parts[3] != 'None' else None
                        status = parts[4]
                        task = App_details(task_id, title, description, due_date, status)
                        self.tasks.append(task)
                    else:
                        print("skipping invalid lines:",line.strip())
            print(f"Task Loaded successfully")
        except FileNotFoundError:
            print("File not found.No tasks to load.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

print("Welcome to the To-do Aplication!")
print("1. Add a new task")
print("2. View all tasks")
print("3. Update a task")
print("4. Delete a task")
print("5. Filter tasks by status")
print("6. Save tasks")
print("7. Load tasks")
print("8. Exit")
manager=AppManager()
while True:
    try:
        user_info=int(input("Enter your choice:"))
        if user_info==1:
            manager.new_tasks()
        elif user_info==2:
            manager.view()
        elif user_info==3:
            manager.update()
        elif user_info==4:
            manager.delete()
        elif user_info==5:
            manager.filter()
        elif user_info==6:
            manager.save()
        elif user_info==7:
            manager.Load()
    except ValueError:
        print("Invalid input. Please enter valid input")





