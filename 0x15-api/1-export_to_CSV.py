#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info 
    all tasks owned by an employee are saved to csv format """

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = get(user_url + id).json()
    to_dos = get(to_do_url + id).json()

    filename = id + ".csv"

    with open(filename, mode='w') as export_file:
        writer = csv.writer(export_file, quoting=csv.QUOTE_ALL)
        for task in to_dos:
            writer.writerow([task["userId"], user["username"],
                            task["completed"], task["title"]])
