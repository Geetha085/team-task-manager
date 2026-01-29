from storage import save_task

def add_task(task):
    save_task(task)
    print(f"Task saved: {task}")
