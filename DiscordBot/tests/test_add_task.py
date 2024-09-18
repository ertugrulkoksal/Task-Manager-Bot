import database

def test_add_task():
    task_id = database.add_task("Test Görevi")
    assert isinstance(task_id, int)
