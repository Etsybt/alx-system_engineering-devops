#!/usr/bin/python3
"""Retrieves data from REST API and exports it in CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id))
    employee_name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = employee_id + '.csv'
    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(employee_id):
                writer.writerow([employee_id, employee_name, str(
                    task.get('completed')),
                                 task.get('title')])
