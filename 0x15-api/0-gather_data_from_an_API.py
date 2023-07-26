#!/usr/bin/python3
"""
Script that returns information from REST API
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv, exit

    try:
        id = argv[1]
        is_int = int(id)
    except BaseException:
        exit()

    # API endpoints for the user and todo details based on the provided user
    # ID.
    url_user = "https://jsonplaceholder.typicode.com/users?id=" + id
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + id

    # Send GET request to the API endpoints.
    r_user = get(url_user)
    r_todo = get(url_todo)

    try:
        # Parse the JSON response data.
        js_user = r_user.json()
        js_todo = r_todo.json()

    if js_user and js_todo:
        # Extract relevant information from the JSON data.
        EMPLOYEE_NAME = js_user[0].get('name')
        TOTAL_NUMBER_OF_TASKS = len(js_todo)
        NUMBER_OF_DONE_TASKS = sum(item.get("completed")
                                   for item in js_todo if item)

        # Print the retrieved information in a formatted manner.
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBEROF_TASKS))
        for todo in js_todo:
            TASK_TITLE = todo.get('title')
            if todo.get("completed"):
                print("\t {}".format(TASK_TITLE))
