#!/usr/bin/python3
"""Script that returns information from REST API"""


if __name__ == "__main__":
    from requests import get
    from sys import argv, exit

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users?id=/{}".format(base_url) + employee_id
    todo_url = "{}/todos?userId={}".format(base_url) + employee_id

    employee_details = request.get(employee_url)
    todo_details = request.get(todo_url)

    try:
        json_usr = employee_details.json()
        json_todo = todo_details.json()
    except ValueError:
        print("Not a Json file")

    if json_usr and json_todo:
        name = json_usr[0].get('name')
        total_tasks = len(json_todo)
        tasks_done = sum(task.get("completed")
                         for task in json_todo if task)

        print("Employee {} is done with taskss({}/{}):".format(name,
              tasks_done, total_tasks))

        for todo in json_todo:
            task_title = todo.get('title')
            if todo.get("completed"):
                print("\t {}".format(task_title))

    try:
        employee_id = int(argv[1])
    except ValueError:
        exit(1)
