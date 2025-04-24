import csv
import os

tasks = []  # This will hold tasks in memory
filename = "tasks.csv"

# Load existing tasks from file (if any)
if os.path.exists(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            task = {
                "title": row[0],
                "description": row[1],
                "due_date": row[2],
                "priority": row[3],
                "status": row[4]
            }
            tasks.append(task)

# Function to add task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter task priority (1-5): ")

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, description, due_date, priority, "pending"])

    print("Task added successfully!")

# Function to list tasks
def list_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n--- Task List ---")
    i = 1
    for task in tasks:
        print("Task", i)
        print(" Title:", task["title"])
        print(" Description:", task["description"])
        print(" Due Date:", task["due_date"])
        print(" Priority:", task["priority"])
        print(" Status:", task["status"])
        print("-" * 25)
        i += 1

# Function to mark task as completed
def mark_task():
    list_tasks()
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "completed"
            # Rewrite the updated list back to the file
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                for task in tasks:
                    writer.writerow([
                        task["title"],
                        task["description"],
                        task["due_date"],
                        task["priority"],
                        task["status"]
                    ])
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    print("\n--- Simple To-Do App ---")
    print("Commands: add | list | mark | exit")
    command = input("Enter command: ").lower()

    if command == "add":
        add_task()
    elif command == "list":
        list_tasks()
    elif command == "mark":
        mark_task()
    elif command == "exit":
        print("Exiting To-Do App")
        break
    else:
        print("Invalid command. Please try again.")
