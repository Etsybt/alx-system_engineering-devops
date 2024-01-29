#!/usr/bin/python3
"""Retrieves data from REST API and exports it in JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    employee_tasks = {}
    task_list = []

    for task in todos:
        if task.get('userId') == int(employee_id):
            task_dict = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.json().get('username')}
            task_list.append(task_dict)
    employee_tasks[employee_id] = task_list

    filename = employee_id + '.json'
    with open(filename, mode='w') as file:
        json.dump(employee_tasks, file)
