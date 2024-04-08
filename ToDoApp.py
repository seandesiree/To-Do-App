to_do_list = []
completed_tasks = []


def add_task():
    new_items = input("What task would you like to add? ")
    to_do_list.append(new_items)

def view_task():
    print(f"Completed tasks: {completed_tasks}")
    print(f"Task to complete: {to_do_list}")

def mark_complete():
    mark = input("What task would you like to mark as complete? ")
    to_do_list.remove(mark)
    completed_tasks.append(mark)

def delete():
    deleted_task = input("What task would you like to delete? ")
    if deleted_task in to_do_list:
        to_do_list.remove(deleted_task)
    if deleted_task in completed_tasks:
        completed_tasks.remove(deleted_task)


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
            4. Delete a task
            5. Quit """)
            if menu == "1":
                add_task()
            elif menu == "2":
                view_task()
            elif menu == "3":
                mark_complete()
            elif menu == "4":
                delete()
            elif menu == "5":
               break
        except ValueError:
            print("Please enter a number between 1 - 5. ")

to_do_app()