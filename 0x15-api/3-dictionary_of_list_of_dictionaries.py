#!/usr/bin/python3
# Records all tasks that are owned by this employee
import json
from sys import argv
from requests import get


if __name__ == "__main__":

    userUrl = "https://jsonplaceholder.typicode.com/users"
    taskUrl = "https://jsonplaceholder.typicode.com/todos"

    allUsers = len(get(userUrl).json())

    with open("todo_all_employees.json", "w") as file:
        users_json = {}
        for i in range(0, allUsers):
            user = get(userUrl, params={"id": i+1})
            tasks = get(taskUrl, params={"userId": i+1})
            username = user.json()[0].get("username")
            task_list = []
            for task in tasks.json():
                task_data = {}
                task_data["username"] = username
                task_data["task"] = task.get("title")
                task_data["completed"] = task.get("completed")
                task_list.append(task_data)
            users_json[i+1] = task_list
        json.dump(users_json, file)
