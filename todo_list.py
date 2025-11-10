def add_task(todo_list, task_name):
    """Adds a new task to the to-do list."""
    task = {"name": task_name, "completed": False}
    todo_list.append(task)
    print(f"Task '{task_name}' added.")

def view_tasks(todo_list):
    """Displays all tasks with their completion status."""
    if not todo_list:
        print("Your to-do list is empty!")
        return

    print("\n--- TO-DO LIST ---")
    for index, task in enumerate(todo_list):
        status = "✓" if task["completed"] else " "
        print(f"{index + 1}. [{status}] {task['name']}")
    print("------------------")

def mark_completed(todo_list, task_index):
    """Marks a task as completed based on its index."""
    try:
        # Adjust for 0-based index
        task = todo_list[task_index - 1] 
        task["completed"] = True
        print(f"Task '{task['name']}' marked as completed.")
    except IndexError:
        print("Error: Invalid task number.")

def delete_task(todo_list, task_index):
    """Deletes a task based on its index."""
    try:
        deleted_task = todo_list.pop(task_index - 1)
        print(f"Task '{deleted_task['name']}' deleted.")
    except IndexError:
        print("Error: Invalid task number.")

def main():
    todo_list = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(todo_list, task_name)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            view_tasks(todo_list)
            if todo_list:
                try:
                    task_num = int(input("Enter the number of the task to mark as complete: "))
                    mark_completed(todo_list, task_num)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks(todo_list)
            if todo_list:
                try:
                    task_num = int(input("Enter the number of the task to delete: "))
                    delete_task(todo_list, task_num)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()