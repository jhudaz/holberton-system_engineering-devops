#!/usr/bin/python3
# The script must accept an integer as a parameter, which is the employee ID
import requests
from sys import argv


if __name__ == "__main__":

    user_id = {"id": argv[1]}
    user_id2 = {"userId": argv[1]}

    user_req = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=user_id)
    task_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=user_id2)

    name = user_req.json()[0].get("name")
    completed = [task for task in task_list.json() if task['completed']]
    total = len(task_list.json())
    text = "Employee {} is done with tasks({}/{}):"
    print(text.format(name, len(completed), total))
    for task in completed:
        print("\t{}".format(task['title']))
