#!/usr/bin/python3
# The script must accept an integer as a parameter, which is the employee ID
import csv
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_req = requests.get("{}/users".format(url), params={"id": argv[1]})
    task_list = requests.get("{}/todos".format(url),
                             params={"userId": argv[1]})

    user_id = argv[1]
    username = user_req.json()[0].get('username')

    with open("{}.csv".format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in task_list.json():
            state = row.get("completed")
            title = row.get("title")
            writer.writerow([user_id, username, state, title])
