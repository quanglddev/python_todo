from Task import Task
import uuid #A built-in library, use for task ID generation

allTasks = [] #Initialize a global list (array) to store created tasks

def printMenu(): 
    print("===============================================") 
    print("Welcome to the terminal-based todo list program") 
    print("Press 'n' for adding new task.") 
    print("Press 'check [num] to change task state.") 
    print("Press 'del [num] to delete a task.")
    print("===============================================")

def handleNewTask(): 
    newTaskName = input("What's the new task name: ") #Again we ask for more input 😜
    newTaskID = uuid.uuid4() #This will create a random unique string (because ID is meant to be unique)
    newTask = Task(str(newTaskID)[:8], newTaskName, False) #[:8] we just take the first 8 letters in the unique string because that's enough (2 duplication in 100k generation - good enough). False because every task when created is not done (that's how it works)
    allTasks.append(newTask) #This is how you append an element into a list (array)
    print("Task added.") #Tell the user things are good

def deleteTask(userInput):
	selectedTaskID = userInput.split()[1] #Same logic
	for i in range(len(allTasks)):
		if allTasks[i].taskID == selectedTaskID: #Found it
			del allTasks[i] #Delete the found task, because that's what the user want
			break #This stops the for loop from running, because we already achieved what we want (delete)
	print("Task deleted.")

def handleCheckTask(userInput): #userInput will be like 'c 47814939'
    selectedTaskID = userInput.split()[1] #By splitting, we create a list of words ['c', '47814939']. So [1] means choose the second element, which is the id user specify.
    for i in range(len(allTasks)): #Find the task by loop through it, this is a standard way of loop through a list.
        if allTasks[i].taskID == selectedTaskID: #Found it
            newState = not allTasks[i].isDone #Change state
            allTasks[i].isDone = newState #Change the task that matches the wanted ID

def printTasks(): 
    print("Task count: %d" % (len(allTasks))) #len() is a function to count how many elements in a list
    for task in allTasks: 
	    print(task) #This will run the __str__ that we implement previously
    if len(allTasks) == 0: 
        print("You don't have any tasks coming up. Enjoy life!") #Just some nonsense text


if __name__ == '__main__':
    userInput = "" #Initialize a variable that we can manipulate later
    while userInput.lower() != "exit": #Program keeps running until the user want to quite by enter exit
        printMenu() #Print tutorial so the user knows what to do
        printTasks() 
        userInput = input("Enter your choice: ") #Asking what user wants to do (add/check/delete)
		#Start checking so we can do what the user want
        if userInput.lower() == "n": #User wants to create a new task
            handleNewTask() 
        elif "check" in userInput.lower(): #Python makes easy for us to check if certain keywork is inside a string
            handleCheckTask(userInput.lower()) 
        elif 'del' in userInput.lower(): #Same logic applied
            deleteTask(userInput.lower()) 
        elif userInput.lower() == "exit": 
            pass #Time to say goodbye
        else: 
            print("Unrecognized input detected. Please try again.")
