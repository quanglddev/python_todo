#For storing tasks locally (persistent)
import sqlite3

conn = sqlite3.connect("tasks.db")

c = conn.cursor()

try:
    c.execute('''
    CREATE TABLE tasks (
        taskID text,
        taskName text,
        isDone integer
    )
    ''')
except:
    pass

def getAllTasks():
    with conn: 
        c.execute("SELECT * FROM tasks")
        return c.fetchall()

def insertTask(task):
    with conn:
        c.execute("INSERT INTO tasks VALUES (:taskID, :taskName, :isDone)", (task.taskID, task.taskName, task.isDone))

def updateTaskState(taskID, isDone):
    with conn:
        c.execute("""
        UPDATE tasks SET isDone = :isDone
        WHERE taskID = :taskID
        """, {'isDone': isDone, 'taskID': taskID})

def removeTask(taskID):
    with conn:
        c.execute('''
        DELETE from tasks
        WHERE taskID = :taskID
        ''', {"taskID": taskID})

