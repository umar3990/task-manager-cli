## File: task_manager.py
from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, description):
        task = {"id": len(self.tasks)+1, "desc": description, "done": False}
        self.tasks.append(task)
        save_tasks(self.tasks)
        print(f"Task added: {task['desc']}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            print(f"[{status}] {task['id']}: {task['desc']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks(self.tasks)
                print(f"Task {task_id} marked as complete.")
                return
        print("Task ID not found.")

    def delete_task(self, task_id):
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < original_len:
            save_tasks(self.tasks)
            print(f"Task {task_id} deleted.")
        else:
            print("Task ID not found.")