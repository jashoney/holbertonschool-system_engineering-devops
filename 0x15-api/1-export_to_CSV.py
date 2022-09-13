#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info
    all tasks owned by an employee are saved to csv """

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = requests.get(user_url + id).json()
    to_dos = requests.get(to_do_url + id).json()
    filename = f"{id}.csv"
    with open(filename, 'w', newline="") as export_file:
        tasks = csv.writer(export_file, quoting=csv.QUOTE_ALL)
        for task in to_dos:
            tasks.writerow([int(id),
                            user.get("username"),
                            task.get("completed"),
                            task.get("title")])
