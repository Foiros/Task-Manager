import os.path
from os import path
import time


def write_into_file(file_name, task_ID, task):
    # If the file exist, we can modify it
    if path.exists(file_name):
        file = open(file_name, 'a')
        text = task_ID + ". " + task + "\n"
        file.write(text)
        file.close()
    # If the while doesn't exist, we will create it
    else:
        file = open(file_name, 'w')
        text = task_ID + ". " + task + "\n"
        file.write(text)
        file.close()


def read_file(file_name):
    # If the file exist, we will read it
    if path.exists(file_name):
        file = open(file_name)
        print("Tehtävät tänään: ")
        print(file.read())
        time.sleep(2)
        file.close()
    # Else we will inform the user that the taks list doesn't exist.
    else:
        print("Task list doesn't exist!")
        time.sleep(2)


def remove_file(file_name):
    # If list exists, we will remove it
    # else we will yell at user (me) that there is no file to remove
    if path.exists(file_name):
        os.remove(file_name)
    else:
        print("Task list doesn't exist!")
        time.sleep(2)
