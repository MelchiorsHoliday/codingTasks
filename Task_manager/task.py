import datetime
import task_list
import sys
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


class Task:
    """
    Class representing a task with title, date, time, completion status,"
    "and due date.
    """

    def __init__(self, title, date, time, complete, due):
        """
        Initialize a Task object.

        Parameters:
        - title (str): The title of the task.
        - date (str or datetime.date): The date of the task.
        - time (str or datetime.time): The time of the task.
        - complete (bool): The completion status of the task.
        - due (str or datetime.date): The due date of the task.
        """
        self.title = title
        self.date = date
        self.time = time
        self.complete = complete
        self.due = due

    @staticmethod
    def delete_task():
        """
        Deletes a task from the task list.
        """
        if len(task_list.existing_tasks) != 0:
            deletion_choice = input("Please type the title of the task you"
                                    "wish to delete:\n")
            for index, tasks in enumerate(task_list.existing_tasks):
                if tasks.title == deletion_choice:
                    del task_list.existing_tasks[index]
                    break
            else:
                print("Task not found")
        else:
            print("There are no tasks")

    @staticmethod
    def task_complete():
        """
        Marks a task as complete.
        """
        if len(task_list.existing_tasks) != 0:
            choice = input("Please type the title of the task you wish to mark"
                           "as complete:\n")
            for index, tasks in enumerate(task_list.existing_tasks):
                if tasks.title == choice:
                    task_list.existing_tasks[index].complete = True
                    break
            else:
                print("Task not found")
        else:
            print("There are no tasks")


def make_task():
    """
    Creates a new task based on user input.
    """
    # Title of task
    new_title = input("What is the name of the task? ")
    # Date of creation
    new_date = input("Is the task for today, yes or no? ")
    if new_date.lower() == "yes":
        new_date = datetime.date.today()
    else:
        new_date = input("What date is the task for? ")
    # Time of creation
    new_time = input("Does the task begin right now, yes or no? ")
    if new_time.lower() == "yes":
        new_time = datetime.datetime.now().strftime("%H:%M")
    else:
        new_time = input("What time does the task begin? ")
    # Complete status
    new_complete = False
    # Due date
    new_due = input("When is it due? ")
    # Creating the class object
    new_task = Task(new_title, new_date, new_time, new_complete, new_due)
    task_list.existing_tasks.append(new_task)
