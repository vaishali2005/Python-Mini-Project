def MainMenu(Menu):
    menu_str = '\t'.join(Menu)
    print(menu_str)
    action =  input("Select which action you want to perform in your to do list : ").strip().capitalize()
    if action not in Menu:
        print(f"{action} task not exist")
    else:
        return action
    
    
def addTask():
    with open("Project\ToDoList.txt","a") as f:
        data = input("Add new To Do item : ").capitalize()
        eof = "\n"
        f.write(data+eof)
        print("Sucessfully Added!")
        f.close()

def ViewTask():
    with open("Project\ToDoList.txt","r") as f:
        data = f.read()
        print(data)
        f.close()
            
def  DeleteTask():
    task = input("Enter the item you want to remove : ").capitalize()
    with open("Project\ToDoList.txt","r") as f:
        data = f.readlines() 
        # new_data = [d for d in data if d.strip() != task]
        # if len(new_data) < len(data):
        #     with open("Project\ToDoList.txt","w") as f:
        #         f.writelines(new_data)
        #         print(f"{task} has removed from list")
        # else:
        #         print(f"{task} was not found in list")
        
        # print(data)
        with open("Project\ToDoList.txt","w") as f:
            find = False
            for d in data:
               if d.strip() != task:
                   f.write(d)
               else:
                   find = True
        if find:
            print(f"{task} has removed from list")
        else:
            print(f"{task} was not found in list")
        f.close() 

               
def ToDoList(action):
    match action:
        case 'Add':
            addTask()
            action = MainMenu(Menu)
            ToDoList(action)
        case 'View':
            ViewTask()
            action = MainMenu(Menu)
            ToDoList(action)
        case 'Delete':
            DeleteTask()
            action = MainMenu(Menu)
            ToDoList(action)
        case 'Exit':
            print("You are exit")
            exit()            
        
print(f"Welcome to Your To Do List, name")
Menu = ['Add', 'View', 'Delete', 'Exit']
# ToDoList(Menu)
for m in Menu:
    action = MainMenu(Menu)
    ToDoList(action)
