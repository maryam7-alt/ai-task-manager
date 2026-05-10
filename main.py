from storage import load_tasks
from tasks import add_task, delete_task, mark_completed
from api import get_quote, get_time
import uuid

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            task = {
                "id": str(uuid.uuid4()), 
                "title": title,
                "quote": get_quote(),
                "created_at": get_time(),
                "completed": False
            }
            tasks = add_task(tasks, task)

        elif choice == "2":
            for t in tasks:
                print(t)

        elif choice == "3":
            task_id = int(input("Task ID: "))
            tasks = mark_completed(tasks, task_id)

        elif choice == "4":
            task_id = int(input("Task ID: "))
            tasks = delete_task(tasks, task_id)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()