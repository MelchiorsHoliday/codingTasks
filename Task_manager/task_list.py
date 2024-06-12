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

existing_tasks = []


def print_tasks():
    for number, task in enumerate(existing_tasks):
        print("\n-------------------\n")
        print(f"Task number {number}")
        print(f"Title: {task.title}")
        print(f"Date: {task.date}")
        print(f"Time: {task.time}")
        print(f"Complete: {task.complete}")
        print(f"Due: {task.due}")
        print("\n^^^^^^^^^^^^^^^^^^^\n")
