#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info
    program accepts an interger as a parameter
    identifying the employee
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = get(user_url + id).json()
    to_dos = get(to_do_url + id).json()

    total_tasks = 0
    tasks_completed = 0
    tasks_done_list = []
    for task in to_dos:
        total_tasks += 1
        if task["completed"] is True:
            tasks_completed += 1
            tasks_done_list.append(task["title"])

    name = user['name']

    print("Employee {} is done with tasks({}/{}):".
          format(name, tasks_completed, total_tasks))
    for task in tasks_done_list:
        print("\t {}".format(task))
