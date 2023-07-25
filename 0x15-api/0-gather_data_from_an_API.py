#!/usr/bin/python3
"""
Script that returns information from REST API

"""


if __name__ == "__main__":
    import os
    from requests import get
    from sys import argv, exit


    def get_employee_todo_progress(employee_id):
        """
        Fetches and displays the todo list of an employee

        Parameters:
            employee_id (int): ID to the employee.

        Returns:
            None
        """
        base_url = "https://jsonplaceholder.typicode.com"
        employee_url = "{}/users?id=/{:d}".format(base_url) + emp_id
        todo_url = "{}/todos?userId={:d}".format(base_url) + emp_id

        try:
            # Fetch employee information
            employee_response = requests.get(employee_url)
            employee_data = employee_response.json()
            employee_name = employee_data.get('name', 'Unknown Employee')

            # Fetch tasks information
            tasks_response = requests.get(task_url)
            tasks_data = tasks_response.json()
            total_tasks = len(tasks_data)
            completed_tasks = [
                task for task in tasks_data if task.get(
                    'completed', False)]
            num_completed_tasks = len(completed_tasks)

            # Display the progress
            print("Employee {} is done with tasks({}/{}):".format(employee_name,
                  num_completed, total_tasks))
            for task in completed_tasks:
                print("\t {}".format(task_title))
