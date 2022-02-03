import os.path
from os import path
import time


def write_into_file(file_name, task_ID, task):
    if path.exists(file_name):
        file = open(file_name, 'a')
        text = task_ID + ". " + task + "\n"
        file.write(text)
        file.close()
    else:
        file = open(file_name, 'w')
        text = task_ID + ". " + task + "\n"
        file.write(text)
        file.close()


def read_file(file_name):
    if path.exists(file_name):
        file = open(file_name)
        print("Tehtävät tänään: ")
        print(file.read())
        time.sleep(2)
        file.close()
    else:
        print("Task list doesn't exist!")
        time.sleep(2)


def remove_file(file_name):
    if path.exists(file_name):
        os.remove(file_name)
    else:
        print("Task list doesn't exist!")
        time.sleep(2)
