tasks = []

def show_menu():
    print("\n--- TODO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        print("\nYour tasks: ")
        for i,task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added: '{task}'")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Deleted '{removed}'")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option(1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == '__main__':
    main()