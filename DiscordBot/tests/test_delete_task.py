import database

def test_delete_task():
    task_id = database.add_task("Test Silme")
    database.delete_task(task_id)
    tasks = database.show_tasks()
    assert all(task['id'] != task_id for task in tasks)
