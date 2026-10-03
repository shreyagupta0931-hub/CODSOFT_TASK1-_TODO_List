# CodSoft Python Programming Internship
# Task 1: To-Do List Application

tasks = []


def add_task():
    print("\n--- ADD TASK ---")

    title = input("Enter a new task: ").strip()

    if title == "":
        print("Task cannot be empty.")
    else:
        task = {
            "title": title,
            "completed": False
        }

        tasks.append(task)

        print("\nTask added successfully!")
        print("Task:", title)


def view_tasks():
    print("\n--- YOUR TASKS ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['title']} - {status}")


def update_task():
    print("\n--- UPDATE TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to update: "))

        if 1 <= number <= len(tasks):

            new_title = input("Enter new task name: ").strip()

            if new_title == "":
                print("Task cannot be empty.")
            else:
                tasks[number - 1]["title"] = new_title
                print("\nTask updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    print("\n--- DELETE TASK ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):

            deleted_task = tasks.pop(number - 1)

            print("\nTask deleted successfully!")
            print("Deleted:", deleted_task["title"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    print("\n--- MARK TASK AS COMPLETED ---")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(
            input("\nEnter task number to mark as completed: ")
        )

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            print("\nTask marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():

    while True:

        print("\n==============================")
        print("        TO-DO LIST APP")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            print("\nThank you for using To-Do List App!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
