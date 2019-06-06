from Task import Task
import DatabaseHandler as db

import colored
from colored import stylize

import uuid

#For clearing terminal
from os import system, name 

# import sleep to show output for some time period 
from time import sleep

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

tasks = []

def syncSQLtoMemory():
    global tasks
    tasks = []
    savedTasks = db.getAllTasks()
    for savedTask in savedTasks:
        tasks.append(Task(savedTask[0], savedTask[1], savedTask[2]))

syncSQLtoMemory()

def printMenu():
    sleep(1)
    clear()
    print(stylize("===============================================", colored.fg("yellow")))
    print(stylize("Welcome to the terminal-based todo list program", colored.fg("hot_pink_1a")))
    print(stylize("Press 'n' or 'new' for adding new task.", colored.fg("blue")))
    print(stylize("Press 'c [num] or check [number]' to change task state.", colored.fg("green")))
    print(stylize("Press 'd [num] or del [number]' to delete a task.", colored.fg("red")))
    print(stylize("===============================================", colored.fg("yellow")))

def printTasks():
    print(stylize("Task count: %d" % (len(tasks)), colored.fg("light_yellow_3")))
    for task in tasks:
        print(stylize(task, colored.fg("light_yellow")))
    if len(tasks) == 0:
        print(stylize("You don't have any tasks coming up. Enjoy life!", colored.fg("spring_green_4")))

def handleNewTask():
    taskNameValid = False
    newTaskName = ""
    while not taskNameValid:
        newTaskName = input(stylize("What's the new task name: ", colored.fg("light_yellow_3")))
        if newTaskName.strip() != "":
            taskNameValid = True
        else:
            print(stylize("Task name cannot be blanked. Please try again.", colored.fg("red")))
    newTaskID = uuid.uuid4()
    newTask = Task(str(newTaskID)[:8], newTaskName, False)
    tasks.append(newTask)
    db.insertTask(newTask)
    print(stylize("Task added.", colored.fg("green")))

def handleCheckTask(userInput):
    tasksIDPendingChecked = userInput.split()
    del tasksIDPendingChecked[0] #Because the first element will be 'check'
    #tasksIDPendingChecked = list(map(int, tasksIDPendingChecked))
    for taskID in tasksIDPendingChecked:
        for i in range(len(tasks)):
            if tasks[i].taskID == taskID:
                newState = not tasks[i].isDone
                tasks[i].isDone = newState
                db.updateTaskState(tasks[i].taskID, newState)

def deleteTask(userInput):
    tasksIDPendingDelete = userInput.split()
    del tasksIDPendingDelete[0] #Because the first element will be 'del'
    #tasksIDPendingDelete = list(map(int, tasksIDPendingDelete))
    for taskID in tasksIDPendingDelete:
        db.removeTask(taskID)
    syncSQLtoMemory()
    print(stylize("Task deleted.", colored.fg("green")))

if __name__ == "__main__":
    userInput = ""
    while userInput.lower() != "exit" and userInput.lower() != "quit":
        printMenu()
        printTasks()
        userInput = input(stylize("Enter your choice: ", colored.fg("light_yellow_3")))
        if userInput.lower() == "n" or userInput.lower() == "new":
            try:
                handleNewTask()
            except:
                print("Error 101. Please refer to the developer for immediate fix. Sorry for the inconvenience.")
        elif "check" in userInput.lower() or userInput.lower().split()[0] == "c":
            try:
                handleCheckTask(userInput.lower())
            except:
                print("Error 102. Please refer to the developer for immediate fix. Sorry for the inconvenience.")
        elif 'del' in userInput.lower()  or userInput.lower().split()[0] == "d":
            try:
                deleteTask(userInput.lower())
            except:
                print("Error 103. Please refer to the developer for immediate fix. Sorry for the inconvenience.")
        elif userInput.lower() == "exit" or userInput.lower() == "quit":
            pass
        else:
            print(stylize("Unrecognized input detected. Please try again.", colored.fg("red")))
    clear()
    print(stylize("Farewell!!!", colored.fg("green")))