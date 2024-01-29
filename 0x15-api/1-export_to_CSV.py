#!/usr/bin/python3

"""
This Python script utilizes a REST API to fetch information
regarding the progress of a given employee's TODO list.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    # Fetching TODOs and users data
    todos_response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()
    users_response = get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Finding the employee by ID
    employee_name = None
    for user in users_data:
        if user.get('id') == int(argv[1]):
            employee_name = user.get('name')
            break

    if employee_name:
        # Filtering tasks owned by the employee
        tasks = []
        for todo in todos_data:
            if todo.get('userId') == int(argv[1]):
                tasks.append(todo)

        # Writing tasks to CSV file
        filename = "{}.csv".format(argv[1])
        with open(filename, 'w') as csvfile:
            for task in tasks:
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                    task['userId'], employee_name, str(
                        task['completed']), task['title']
                ))

        print("Data exported to", filename)
    else:
        print("Employee not found.")
