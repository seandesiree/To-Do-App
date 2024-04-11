to_do_list = []
completed_tasks = []
high_priority = []


def add_task():
    new_items = input("What task would you like to add? ")
    to_do_list.append(new_items)

def view_task():
    print(f"Completed tasks: {completed_tasks}")
    print(f"Task to complete: {to_do_list}")
    print(f"High priority tasks: {high_priority}")

def mark_complete():
    mark = input("What task would you like to mark as complete? ")
    if mark not in completed_tasks:
        completed_tasks.append(mark) 
        if mark in to_do_list:
            to_do_list.remove(mark)
        elif mark in high_priority:
            high_priority.remove(mark)
    
def delete():
    deleted_task = input("What task would you like to delete? ")
    if deleted_task in to_do_list:
        to_do_list.remove(deleted_task)
    if deleted_task in completed_tasks:
        completed_tasks.remove(deleted_task)

def priority():
    priority = input("What task would you like to mark as high priority? ")
    if priority in to_do_list:
        high_priority.append(priority)
        to_do_list.remove(priority)


def to_do_app():
    while True:
        try:
            menu = input("""              
            Welcome to your To Do List!
            The perfect helper to stay on task and productive!
            Here are your options.
            Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Mark as high priority
            5. Delete a task
            6. Quit """)
            if menu == "1":
                add_task()
            elif menu == "2":
                view_task()
            elif menu == "3":
                mark_complete()
            elif menu == "4":
                priority()
            elif menu == "5":
                delete()
            elif menu == "6":
               break
        except ValueError:
            print("Please enter a number between 1 - 5. ")

to_do_app()