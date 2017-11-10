import numpy as np


def put(self, todo_id):
    args = parser.parse_args()
    task = {'task': args['task']}
    TODOS[todo_id] = task
    return task, 201




