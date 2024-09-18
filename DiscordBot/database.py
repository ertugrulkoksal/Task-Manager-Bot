import sqlite3

def connect_db():
    return sqlite3.connect('data.db')

def create_table():
    with connect_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)))''')

def add_task(description):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
        conn.commit()
        return cursor.lastrowid

def delete_task(task_id):
    with connect_db() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def show_tasks():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, description, completed FROM tasks")
        return [{'id': row[0], 'description': row[1], 'completed': bool(row[2])} for row in cursor.fetchall()]

def complete_task(task_id):
    with connect_db() as conn:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()

create_table()
