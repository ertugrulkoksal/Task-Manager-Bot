import database

def test_complete_task():
    task_id = database.add_task("Test Tamamlama")
    database.complete_task(task_id)
    tasks = database.show_tasks()
    for task in tasks:
        if task['id'] == task_id:
            assert task['completed'] == True
