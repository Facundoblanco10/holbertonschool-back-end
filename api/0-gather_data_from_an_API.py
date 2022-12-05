#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,"""
"""returns information about his/her TODO list progress."""
import json
from urllib import request
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = request.urlopen("https://jsonplaceholder.typicode.com"
               "/users/{}".format(user_id))
    tasks_url = request.urlopen("https://jsonplaceholder.typicode.com"
               "/todos?userId={}".format(user_id))
    user = user_url.read().decode("utf-8")
    tasks = tasks_url.read().decode("utf-8")
    user = json.loads(user)
    tasks = json.loads(tasks)
    tasks_completed = []
    for i in tasks:
        if i["completed"]:
            tasks_completed.append(i)
    print("Employee {} is done with tasks({}/{}):".format(user["name"],
                                                          len(tasks_completed),
                                                          len(tasks)))

    for task in tasks_completed:
        print("\t {}".format(task["title"]))