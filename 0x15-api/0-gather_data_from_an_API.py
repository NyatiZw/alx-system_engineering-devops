#!/usr/bin/python3
"""Script that returns information from REST API"""


if __name__ == "__main__":
    from requests import get
    from sys import argv, exit

    emp_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users?id=/{}".format(base_url) + emp_id
    todo_url = "{}/todos?userId={}".format(base_url) + emp_id

    employee_details = requests.get(employee_url)
    todo_details = requests.get(todo_url)

    try:
        json_usr = employee_details.json()
        json_todo = todo_details.json()
    except ValueError:

    if json_usr and json_todo:
        name = json_usr[0].get('name')
        total_tasks = len(json_todo)
        tasks_done = sum(task.get("completed")
                         for task in json_todo if task)

        print("Employee {} is done with tasks({}/{}):".format(name,
              tasks_done, total_tasks))

        for todo in json_todo:
            task_title = todo.get('title')
            if todo.get("completed"):
                print("\t {}".format(task_title))
