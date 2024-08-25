to_do_list={}
completed_tasks={}
def add_task(x,y):
     to_do_list[x]=y
def view_tasks():
    print(to_do_list)             
def mark_task_complete(v):
     completed_tasks[v]=to_do_list[v]       
     print("you have completed the taskkk :)")
def delete_task(R):
     del to_do_list[R] 
while 1:
     a=input("do you want to add a new task "
             "or view all tasks "
             "or delete a task "
             "or mark a task completed : ")
     try:
         a=="add a new task" or "view all tasks" or "delete a task" or "mark a task completed"
     except:
         print("please enter what do you want again")
         break 
     if a=="add a new task":
        x=input("enter the new task:")
        y=input("where to enter the task(the value):")
        add_task(x,y) 
     elif a=="delete a task":
         R=input("enter the task you want to delete:")
         delete_task(R)
     elif a=="mark a task completed":
         v=input("enter the task you want to mark completed:") 
         mark_task_complete(v)
     elif a=="view all tasks":
         view_tasks()
     elif a=="exit":
         break
