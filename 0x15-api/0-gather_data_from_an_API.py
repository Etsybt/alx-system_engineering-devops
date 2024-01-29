#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_todo_list(employee_id):
    """fetches a list"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()

        if user_response.status_code != 200 or \
                todo_response.status_code != 200:
            print("Error: Failed to fetch data from the API")
            return

        name = user_data.get('name')
        todos_done = [todo for todo in todo_data if todo.get('completed')]
        total_tasks = len(todo_data)
        tasks_done = len(todos_done)

        print(f"Employee {name} is done with tasks"
              f"({tasks_done}/{total_tasks}):")
        for todo in todos_done:
            print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    fetch_todo_list(int(employee_id))
