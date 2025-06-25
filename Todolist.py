def list():
    tasks = []  #empty list
    print("Welcome To To Do List")

    total_task = int(input("Enter total number of task:"))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        
    print(f"Today's Tasks are\n{tasks}")
    
    while True:
#ADD OF TASK
        operation = int(input("Enter:-\n1-Create new task\n2-Update existing task\n3-Delete Task\n4-View All Tasks\n5-EXIT List\n"))
        if operation == 1:
            add = input("Enter new task:")
            tasks.append(add)
            print(f"Task {add} has been successfully added")
#UPDATE OF TASK
        elif operation == 2:
            updated_val = input("Enter task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task =")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}") 
#DELETE OF TASK
        elif operation == 3:
            del_value = input("Enter Task you want to delete: ")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} is successfully deleted.")
#VIEW ALL TASKS
        elif operation == 4:
            print(f"Total tasks = {tasks}")
#EXIT
        elif operation == 5:
            print("Closing the list!!")
            break

        else:
            print("!Invalid Input....Try again!")

list()
