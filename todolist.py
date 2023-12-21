import os
import pickle


def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Save and Exit")


def load_todo_list():
    if os.path.exists("todo_list.pkl"):
        with open("todo_list.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []


def save_todo_list(todo_list):
    with open("todo_list.pkl", "wb") as file:
        pickle.dump(todo_list, file)


def view_todo_list(todo_list):
    print("\n===== To-Do List =====")
    if not todo_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")


def update_task(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to update: ")) - 1
    if 0 <= index < len(todo_list):
        new_task = input("Enter the new task: ")
        todo_list[index] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def remove_task(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task number.")


def main():
    todo_list = load_todo_list()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            update_task(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            save_todo_list(todo_list)
            print("To-Do List saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
