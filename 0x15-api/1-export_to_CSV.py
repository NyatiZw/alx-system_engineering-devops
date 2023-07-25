#!/usr/bin/python3
"""
Script that returns information from REST API
Exports a CSV file
"""

import csv
import requests
from sys import argv


def to_csv():
    """Function that returns tne API data"""
    usr = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in usr.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to csv"""
    fp = "{}.csv".format(argv[1])
    with open(fp, "w") as csvfile:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"]
        filewriter = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL)
        filewriter.writeheader()
        for task in TASK_STATUS_TITLE:
            filewriter.writerow({"USER_ID": argv[1],
                                 "USERNAME": USERNAME,
                                 "TASK_COMPLETED_STATUS": task[0],
                                 "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
