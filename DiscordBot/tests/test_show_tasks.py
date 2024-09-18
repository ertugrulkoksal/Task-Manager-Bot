import database

def test_show_tasks():
    tasks = database.show_tasks()
    assert isinstance(tasks, list)
