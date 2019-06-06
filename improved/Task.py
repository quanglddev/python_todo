class Task:
    def __init__(self, taskID, taskName, isDone):
        self.taskID = taskID
        self.taskName = taskName
        self.isDone = isDone


    def __str__(self):
        result = ""
        result += ('%s: ' % (self.taskID))
        if self.isDone:
            result += "✅  "
        else:
            result += "⭕️  "
        result += self.taskName
        return result