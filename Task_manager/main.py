import user
import menu
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


def main():
    """
    Main entry point of the program.
    """
    if __name__ == "__main__":
        active_user = user.get_user()  # Get the active user
        menu.main_menu()  # Display the main menu


main()  # Execute the main function when the script is run
