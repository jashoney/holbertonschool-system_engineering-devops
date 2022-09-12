#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info """

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
    tasks_string = f"({len(tasks_done)}/{len(to_dos)}):"
    print(f"Employee {name} is done with tasks {tasks_string}")
    print("\n".join(f"\t {task}" for task in tasks_done))
