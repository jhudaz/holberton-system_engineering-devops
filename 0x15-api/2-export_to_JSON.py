#!/usr/bin/python3
# Records all tasks that are owned by this employee
import json
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_req = requests.get("{}/users".format(url), params={"id": argv[1]})
    task_list = requests.get("{}/todos".format(url),
                             params={"userId": argv[1]})

    user_id = argv[1]
    username = user_req.json()[0].get('username')

    with open("{}.json".format(argv[1]), "w", newline='') as file:
        user_json = {}
        list_format = []
        for task in task_list.json():
            task_data = {}
            task_data["task"] = task.get("title")
            task_data["completed"] = task.get("completed")
            task_data["username"] = username
            list_format.append(task_data)
        user_json[user_id] = list_format
        json.dump(user_json, file)
