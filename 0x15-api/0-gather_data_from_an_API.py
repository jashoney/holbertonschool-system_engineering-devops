#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info
    program accepts an interger as a parameter
    identifying the employee
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = requests.get(user_url + id).json()
    to_dos = requests.get(to_do_url + id).json()

    tasks_done = []
    for task in to_dos:
        if task.get("completed") is True:
            tasks_done.append(task.get("title"))

    name = user.get('name')

    print("Employee {} is done with tasks ({}/{}):".
          format(name, len(tasks_done), len(to_dos)))
    for task in tasks_done:
        print("\t {}".format(task))
