import json
from task import Task

file_name = 'tasks.json'

def load_tasks():
    try:
        with open(file_name,'r') as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(file_name,'w') as file:
        json.dump([task.to_dict()for task in tasks] ,file, indent=4)