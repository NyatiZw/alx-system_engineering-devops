#!/usr/bin/python3
"""Script that returns information from REST API"""

import requests
import os


def get_emp_todo(employee_id):
    """Function to get todo progress"""
    base_url = "https://jsonplaceholder.typicode.com/todos/1"
    employee_url = "{}/employees/{}".format(base_url, employee_id)
    tasks_url = "{}/employees/{}/tasks".format(base_url, employee_id)

    try:
        # Fetch empployee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get('name', 'Unknown Employee')

        # Fetch tasks information
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()
        total_tasks = len(tasks_data)
        completed_tasks = [task for task in tasks_data
                           if task.get('completed', False)]
        num_completed_tasks = len(completed_tasks)

        """Display the progress"""
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print("\t{{}['title']}".format(title))

    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)


if __name__ == "__main__":
    employee_id = int(input("Enter the Employee ID: "))
    get_emp_todo(employee_id)
