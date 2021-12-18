#todo list
import os

def clearConsole(): 
    command = 'clear' 
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class List():
    def __init__(self):
        self.tasks = []
    
    def addtask(self, task):
        self.tasks.append(task)
    
    def removetask(self, index):
        if index - 1 in range(len(self.tasks)):
            self.tasks.pop(index - 1)
        else:
            print("Index does not exist!")
    
    def printlist(self):
        print("----TODO LIST----\n")
        if len(self.tasks) != 0:
            for i in range(len(self.tasks)):
                print(i+1, ": ", self.tasks[i], sep='')
        else:
            print("The list is empty.\n")
        print("-----------------")
    

todo = List()
flag = True

with open("tasks.txt", "r") as f:
    for line in f:
        todo.addtask(line)

while(flag):

    clearConsole()
    todo.printlist()

    command = input("Actions:\n(1) Add task\n(2) Remove task\n(3) Save and exit\n")

    while command != "1" and command != "2" and command != "3":
        command = input("Wrong command!\n")
    
    if command == "1":
        task = input("Task: ") + "\n"
        todo.addtask(task)
    elif command == "2":
        index = input("Index: ")
        if index.isnumeric():
            todo.removetask(int(index))
        else:
            print("Please enter a number.")
    elif command == "3":
        #transfer todo list to file
        open('tasks.txt', 'w').close() #erase file contents
        for task in todo.tasks:
            with open("tasks.txt", "a") as f:
                f.write(task)
        flag = False
