import json 
import os 
from datetime import datetime, timedelta


Tasks_File = "tasks.json"

def load_tasks():
    if os.path.exists(Tasks_File):
        with open(Tasks_File, "r") as f:
            return json.load(f)
    return []    

def save_tasks(tasks):
    with open(Tasks_File, "w") as f:
        json.dump(tasks, f, indent=4)

def score_task(task):
    """calculate urgency score = importance_factor/days_left"""        
    importance_map = {"High":3, "Medium":2, "Low":1}
    deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
    days_left = max((deadline-datetime.now()).days, 1)
    return importance_map[task["importance"]]/days_left



def add_task():
    name = input("Task name: ")
    deadline = input("Deadline (YYYY-MM-DD):")
    importance = input("Importance (High/Medium/Low):")

    task = {
        "name" : name,
        "deadline" : deadline,
        "importance" : importance,
        "done" : False
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def list_tasks():
    tasks= load_tasks()
    tasks= sorted(tasks, key=score_task, reverse=True)


    print("\n--- Your Tasks ---")
    for i, t in enumerate(tasks):
        status = "^" if t["done"] else "x"
        print(f"{i+1}. {t['name']} | Deadline: {t['deadline']} | Importance: {t['importance']} | {status}")

def complete_task():
    tasks= load_tasks()
    list_tasks()
    choice = int(input("\nEnter task number to mark as done: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]['done'] = True
        save_tasks(tasks)
        print("Task Completed!")
    else:
        print("invalid choice")




def main():
    while True:
        print("\n--- Smart to-do list ---")
        print("1. Add task")
        print("2. List Tasks")
        print("3. Complete task")
        print("4. Exit")



        choice = input("choose an option: ")
        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()


        elif choice == "3":
            complete_task()
        elif choice == "4":
            break
        else:
            print("Invalid Choice") 


if __name__ == "__main__":
    main()                                                 