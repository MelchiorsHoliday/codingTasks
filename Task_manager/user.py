import sys
import time


def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_input(prompt='', delay=0.01):
    slow_print(prompt, delay)
    return builtins_input()


# Override print and input functions
builtins_print = print
builtins_input = input
print = slow_print
input = slow_input


class User:
    """
    Class representing a user with a name and password.
    """

    def __init__(self, name, password):
        """
        Initialize a User object.

        Parameters:
        - name (str): The name of the user.
        - password (str): The password of the user.
        """
        self.name = name
        self.password = password


def welcome(person):
    """
    Displays a welcome message for the user.

    Parameters:
    - person (User): The User object to welcome.
    """
    print(f"""
          Welcome {person.name}
""")


def get_user():
    """
    Prompts the user to enter their name and password, creates a User object, 
    and displays a welcome message.

    Returns:
    - User: The User object representing the current user.
    """
    user_name = input("Please enter your name: ")
    user_password = input("Please enter a password: ")
    current_user = User(user_name, user_password)
    welcome(current_user)
    return current_user
