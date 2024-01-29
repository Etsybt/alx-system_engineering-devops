#!/usr/bin/python3
"""Retrieves data from REST API and exports it in JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    # Retrieve users and todos from the API
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_response.json()

    # Prepare dictionary to hold all tasks for each user
    all_tasks = {}

    # Iterate over each user
    for user in users_data:
        task_list = []

        # Iterate over each task
        for task in todos_data:
            # Check if the task belongs to the current user
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_dict)

        # Add user's tasks to the dictionary
        all_tasks[user.get('id')] = task_list

    # Write all tasks to a JSON file
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_tasks, file)
