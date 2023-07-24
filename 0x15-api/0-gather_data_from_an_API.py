#!/usr/bin/python3
"""Script that returns information from REST API"""

if __name__ == "__main__":
    import os
    import requests

    def get_emp_todo(n):
        """Function to get todo progress"""
        base_url = 'https://jsonplaceholder.typicode.com/todos/1'
        n = employee_id
        n_det = "{}/employees/{}".format(base_url, n)
        tasks_url = "{}/employees/{}/tasks".format(base_url, n)

        # Fetch employee information
        employee_response = requests.get(n_det)
        employee_data = employee_response.json()
        employee_name = employee_data.get('name', 'n')

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
            print("\t{}".format(task['title']))
