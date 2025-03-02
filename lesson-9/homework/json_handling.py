import json
import csv

# Function to load tasks from a JSON file
def load_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return []

# Function to save tasks back to a JSON file
def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to '{file_name}'.")

# Function to display all tasks
def display_tasks(tasks):
    print(f"{'ID':<5}{'Task':<20}{'Completed':<12}{'Priority':<10}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{task['completed']:<12}{task['priority']:<10}")
    print("-" * 50)

# Function to calculate task completion stats
def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

# Function to convert tasks JSON data to CSV
def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    if not tasks:
        return
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'task', 'completed', 'priority'])
        writer.writeheader()
        writer.writerows(tasks)
    print(f"Tasks have been converted to '{csv_file}'.")

# Main program
def main():
    tasks_file = 'tasks.json'
    tasks = load_tasks(tasks_file)
    
    if tasks:
        
        display_tasks(tasks)

        
        calculate_task_stats(tasks)

        
        save_tasks(tasks_file, tasks)

        
        convert_json_to_csv(tasks_file, 'tasks.csv')

if __name__ == "__main__":
    main()
