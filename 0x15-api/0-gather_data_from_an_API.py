#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    [print("\t{}".format(c)) for c in completed]
