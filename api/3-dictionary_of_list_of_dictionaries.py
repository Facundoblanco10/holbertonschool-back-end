#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,"""
"""returns information about his/her TODO list progress."""


if __name__ == "__main__":
    import json
    from urllib import request

    users_url = request.urlopen("https://jsonplaceholder.typicode.com"
                                "/users")
    users = users_url.read().decode("utf-8")
    users = json.loads(users)
    f = open("todo_all_employees.json", "a")

    user_json = {}
    for user in users:
        tasks_url = request.urlopen("https://jsonplaceholder.typicode.com"
                                    "/todos?userId={}".format(user["id"]))
        tasks = tasks_url.read().decode("utf-8")
        tasks = json.loads(tasks)
        user_json[user["id"]] = []
        tasks_completed = []
        for i in tasks:
            if i["completed"]:
                tasks_completed.append(i)
        for task in tasks:
            user_json[user["id"]].append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            })
    f.write(json.dumps(user_json))
    f.close()
