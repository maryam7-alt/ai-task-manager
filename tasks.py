from storage import save_tasks


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    return tasks


def delete_task(tasks, task_id):
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return tasks


def mark_completed(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
    save_tasks(tasks)
    return tasks
    