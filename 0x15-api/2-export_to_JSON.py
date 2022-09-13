#!/usr/bin/python3
""" exports data to a json file """

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = get(user_url + id).json()
    to_dos = get(to_do_url + id).json()

    tasks_to_do = []
    for task in to_dos:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task['completed']
        task_dict["username"] = user["username"]
        tasks_to_do.append(task_dict)

    user_to_do_dict = {}
    user_to_do_dict[id] = tasks_to_do

    filename = id + ".json"
    with open(filename, 'w') as json_file:
        json.dump(user_to_do_dict, json_file)
