class Todolist:
    def __init__(self) :
        self.tasks = []
        
    def add_task(self,task):
        self.tasks.append({'task': task,'done':False})
        
    def view_tasks(self):
        if not self.tasks:
            print("No task in the to-do list")
        else:
            for index, task in enumerate(self.tasks,start=1):
                status = "Done" if task['done'] else "not done"
                print(f"{index}. {task['task']}-{status}")
    
    def mark_task_done(self,task_index):
        if 0<= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True 
        else:
            print("Invalid task number")
    
    def delete(self,task_index):
        if 0<= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print("Invaild task number")

def main():
    todo_list = Todolist()
    
    while True:
        print("\n To Do Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose Option: ")
        
        if choice == '1':
            task = input("Enter a new tasks: ")
            todo_list.add_task(task)
        elif choice == '2':   
            todo_list.view_tasks()     
        elif choice == '3':       
            task_index = int(input("Enter task number to be mark done: "))-1
            todo_list.mark_task_done(task_index)
        elif choice == '4':        
            task_index = int(input("Enter task number to be deleted: "))-1
            todo_list.delete(task_index)
        elif choice == '5':             
            print("Exiting the app")
            break
        else: 
            print("Invalid Input")
            
if __name__ == "__main__":
    main()  
        