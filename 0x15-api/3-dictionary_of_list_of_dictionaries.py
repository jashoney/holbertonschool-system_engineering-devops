#!/usr/bin/python3
""" uses jsonplaceholder REST api to return info """

import json
import requests

if __name__ == "__main__":
    usernamedict = {}
    userdict = {}
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for user in users:
        userid = user.get("id")
        userdict[userid] = []
        usernamedict[userid] = user.get("username")
    for task in todos:
        taskdict = {}
        userid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(userid)
        userdict.get(userid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
