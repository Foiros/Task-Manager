from os import system, name
import TaskList

# Idea here is to separate these from the main file, so that main is much cleaner and simpler

FILE_PATH = "C:/users/arttu/Desktop/TaskList.txt"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def write():
    task_ID = input("Please enter task ID: ")
    task = input("Write task here: ")
    TaskList.write_into_file(FILE_PATH, task_ID, task)
    user_decision = input("Do you want to write another task? y/n")
    if user_decision == "y":
        clear()
        write()
    else:
        clear()
        pass


def read_input(userinput):
    # We take users input and based on it we determine, what action we take
    if userinput == 1:
        clear()
        TaskList.read_file(FILE_PATH)
    elif userinput == 2:
        clear()
        write()
    elif userinput == 3:
        TaskList.remove_file(FILE_PATH)
        clear()
