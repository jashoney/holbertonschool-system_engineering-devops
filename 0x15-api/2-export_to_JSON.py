#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info
    exports data to json file
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
    name = user.get("username")
    tasks = []
    for task in to_dos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = name
        tasks.append(task_dict)
    json_obj = {}
    json_obj[id] = tasks
    filename = f"{id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
