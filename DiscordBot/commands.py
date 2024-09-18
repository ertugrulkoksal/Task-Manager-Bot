import database

def add_task(description):
    return database.add_task(description)

def delete_task(task_id):
    return database.delete_task(task_id)

def show_tasks():
    return database.show_tasks()

def complete_task(task_id):
    return database.complete_task(task_id)
