#!/usr/bin/python3
""" all tasks owned by an employee are saved to a csv file """

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/"
    to_do_url = "https://jsonplaceholder.typicode.com/todos/?userId="
    user = get(user_url + id).json()
    to_dos = get(to_do_url + id).json()

    csv_filename = id + ".csv"

    with open(csv_filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in to_dos:
            writer.writerow([task['userId'], user['username'],
                            task['completed'], task['title']])
