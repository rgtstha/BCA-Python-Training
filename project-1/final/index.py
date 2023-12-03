# Initialize the to-do list
# all the list are stored in this list
todo_list = []

# we want this loop to run until the user want
# then we also have to create logic to stop the loop


while True:
    # Display menu options
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Mark as Completed")
    print("3. View Tasks")
    print("4. Remove Task")
    print("5. Exit")



    # Get user choice
    choice = input("Enter your choice (1-5): ")



    # user will press any number from 1-5:
    # based on the user's choice following block will be executed

    if choice == "1":
        # Add Task
        task = input("Enter a new task: ")
        todo_list.append({"task": task, "completed": False})


    elif choice == "2":
        # Mark as Completed
        task_index = int(input("Enter the task number to mark as completed: "))

        #user enters the number/index of the task to mark the task as completed

        if task_index >=0 and task_index < len(todo_list):
          # the index user enters should be greater than 0 and less than the length of the list

          # in python we can write this line of code like this
          # if 0 <= task_index and task_index < len(todo_list)
          # whatever you refer , you can do it

            todo_list[task_index]["completed"] = True
        else:
            print("Invalid task number.")


    elif choice == "3":
        # View Tasks
        # in one of the class we learned enumerate() it de-struct/returns index and task
        # example below....

        for index, task in enumerate(todo_list):
            print(f"{index}: {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")
            # This line  displays the index, task description, and completion status



    elif choice == "4":
        # Remove Task
        task_index = int(input("Enter the task number to remove: "))
        if task_index >=0 and task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")


    elif choice == "5":
        # Exit
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

demo_list = ["Complete assignment", "Buy groceries", "Exercise", "Read a book"]

#  enumerate method returns the index and task
#  you can learn unpacking concept


for index, task in enumerate(demo_list):
    print(f"Task {index + 1}: {task}")

