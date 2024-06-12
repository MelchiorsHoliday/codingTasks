import task_list
import user
import sys
import task
import time


def slow_print(text, delay=0.01):
    """
    Slowly prints out text character by character with a specified delay.

    Parameters:
    - text (str): The text to be printed.
    - delay (float): The delay between printing each character
      (default is 0.01 seconds).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_input(prompt='', delay=0.01):
    """
    Slowly prints out a prompt and then waits for user input.

    Parameters:
    - prompt (str): The prompt to be displayed.
    - delay (float): The delay between printing each character
      (default is 0.01 seconds).

    Returns:
    - str: The user input.
    """
    slow_print(prompt, delay)
    return builtins_input()


# Save references to original print and input functions
builtins_print = print
builtins_input = input

# Override print and input functions with slow versions
print = slow_print
input = slow_input


def quit():
    """
    Exits the program.
    """
    sys.exit()


def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    print("""
          >What would you like to do?\n
          >View tasks
          >Change user
          >Quit
          """)
    choice = input("I would like to: ").lower()
    if choice == "view tasks":
        return task_menu()  # Redirect to task menu
    elif choice == "change user":
        user.get_user()  # Invoke user module to change user
        return main_menu()  # Redirect back to main menu
    elif choice == "quit":
        return quit()  # Exit program
    else:
        print("Please select a valid choice")
        return main_menu()  # Prompt again for valid choice if invalid input


def task_menu():
    """
    Displays the task menu and handles user choices related to tasks.
    """
    if len(task_list.existing_tasks) == 0:
        print("There are currently no tasks\n")
    task_list.print_tasks()  # Display existing tasks
    print("""
          What would you like to do?\n
          >Make a task
          >Mark a task as complete
          >Delete a task
          >Go back
    """)
    choice = input("I would like to: ").lower()
    if choice == "make a task":
        task.make_task()  # Invoke task module to create a new task
        return task_menu()  # Redirect back to task menu
    elif choice == "mark a task as complete":
        task.Task.task_complete()  # Invoke task module to mark as complete
        return task_menu()  # Redirect back to task menu
    elif choice == "delete a task":
        task.Task.delete_task()  # Invoke task module to delete a task
        return task_menu()  # Redirect back to task menu
    elif choice == "go back":
        return main_menu()  # Redirect back to main menu
    else:
        print("Please select a valid choice")
        return task_menu()  # Prompt again for valid choice if invalid input
