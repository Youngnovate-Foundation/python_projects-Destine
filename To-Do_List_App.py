# to display current date and day
import datetime


# an empty list to store tasks
tasks = []


# add_task() function to add a task to the list
def add_task(task):

    # append the task to the end of the tasks list
    tasks.append(task)
    # print a new line for better readability
    print("\n")
    # a confirmation message that the task has been added
    print(f"✅ {task} added successfully!")
    print("\n")


# delete_task() function to remove a task from the list that takes an index as argument
def delete_task(index):
    # check if the index is valid, i.e, greater than 0 and less than or equal to the length of the tasks list
    if 0 < index <= len(tasks):
        # pop() method removes and returns the task at the specified index (index - 1 because list is 0-indexed)
        task_to_delete = tasks.pop(index - 1)
        #  confirmation message that the task has been deleted
        print(f"{task_to_delete} deleted from list✅")
    else:
        # error message for an invalid entered task number
        print(f"Input a valid item to delete")


# view_tasks() function to display all tasks in the list
def view_tasks():
    # print a new line for better readability
    print("")
    # check if the tasks list is empty
    if not tasks:
        # if it is empty, print a message indicating there are no tasks, hence nothing to view
        print("No To-Do items added\n➕Add item to view it.")

    else:
        # otherwise print the current date and day using datetime module and f-string formatting
        print(
            f"Your to-do tasks for today, {datetime.datetime.now().strftime("%A")}, {datetime.date.today()}"
        )
        # loop through the tasks list and print each task with its corresponding number
        # i & range() function to generate a sequence of numbers from 0 to length of tasks - 1
        # range is a sequence data type that generates a sequence of numbers within a specified range
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

    # another new line for better readability
    print("")


# mark_completed() function to mark a task as completed and remove it from the list
def mark_completed():
    # first check if the tasks list is empty
    if not tasks:
        # and then print a message indicating there are no tasks available to mark as completed
        print("No tasks available to mark as completed.")
        # and then exit the function
        return

    # if there are tasks available, call the view_tasks() function to display them
    view_tasks()

    # invoke an infinite loop that runs as long as a condition remains true
    while 1 == 1:
        # prompt the user to enter the number of the task they want to mark as completed
        task_index = int(
            input("Enter the number of the task you want to mark as completed: ")
        )
        # check if the entered task number is valid, i.e, greater than 0 and less than or equal to the length of the tasks list
        if 0 < task_index <= len(tasks):
            # if valid, retrieve the task at the specified index and store it in a variable completed_task
            completed_task = tasks[task_index - 1]
            task_ticked = completed_task + "✔️"
            # for task in tasks:
            for i in range(len(tasks)):
                if tasks[i] == completed_task:
                    tasks[i] = task_ticked

                    # print a confirmation message that the task has been marked as completed
                    print(f"✅ Task '{completed_task}' marked as completed!")
                # and then exit the loop
            break

        else:
            # if the entered task number is invalid, print an error message and prompt the user to try again
            print("Invalid task number. Please try again.")


# invoke an infinite loop that runs as long as a condition remains true
# in this case, the condition is always true (1 == 1)
while 1 == 1:
    # a welcoming message and a brief introduction to the app
    print("<<----------|📝WELCOME TO THE YNGVATE MINI TO-DO APP|---------->>")
    print(
        "             What are your goals for today?\n             Let's get started✍️          "
    )

    print(
        """
          Type:
          1 to add a new to-do item to your list➕
          2 to view/ see your to-do items👁️ 
          3 to remove/delete a task❌
          4 to mark a task as completed✔️
          5 to close your to-do app👋
          """
    )

    # prompt the user to input a command
    option = input("Input command: ")
    # this is the valid commands that the user can input stored in a variable commands
    commands = "12345"

    # if the option inputted by the user is alphabetic characters (a-z, A-Z, or other non-numeric characters)
    if option.isalpha():
        # tell user that the input is invalid and they should input a number instead
        print("‼️ ‼️ ‼️ ‼️ ‼️ ‼️ ‼️\nInvalid option. Please input a number.")

    # and if the option inputted by the user is not in the valid commands too (1, 2, 3, 4, 5)
    # tell user that the input is invalid
    elif not option in commands:
        print("‼️ ‼️ ‼️ ‼️ ‼️ ‼️ ‼️\n")
        print("Input a valid command🚫")
        print("‼️ ‼️ ‼️ ‼️ ‼️ ‼️ ‼️\n")

    # if the option inputted by the user is valid, i.e, either 1, 2, 3, 4, or 5
    # execute the corresponding function based on the user's choice

    elif option == "1":
        # if option is "1", prompt the user to enter a task,
        # convert it to title case using title() method,
        # and store it in a variable task
        task = input("Enter a to-do item or task: ").title()
        # pass the task variable to the add_task() function to add it to the tasks list
        add_task(task)

    # and if option is "2",
    # call the view_tasks() function to display all tasks in the list
    elif option == "2":
        view_tasks()

    # and if option is "3",

    elif option == "3":
        # prompt the user to enter the number of the task they want to delete
        # convert the input to an integer using int() function
        # and store it in a variable task_to_delete
        task_to_delete = input("Which item do you want to delete?\n")
        if task_to_delete.isalpha():
            print("Input a valid number🚫")

        else:
            task_to_delete = int(task_to_delete)
            # call the delete_task() function and pass the task_to_delete variable
            # to it to remove the specified task from the tasks list
            delete_task(task_to_delete)

    # and if option is "4",
    elif option == "4":
        # call the mark_completed() function to
        # mark a task as completed and remove it from the list
        mark_completed()
    # and if option is "5",
    else:
        # print a goodbye message
        print("<<----------|👋THANK YOU FOR USING YNGVATE MINI TO-DO APP|---------->>")
        print("Have a wonderful and fulfilled day🎊\nByeee👋")
        print("Love Destine from YNGVATE❤️")
        # exit the loop and terminate the program
        break
