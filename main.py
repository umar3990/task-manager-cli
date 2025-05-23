## File: main.py
from task_manager import TaskManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Task Manager")
    parser.add_argument("command", choices=["add", "list", "complete", "delete"], help="Command to run")
    parser.add_argument("--task", type=str, help="Task description")
    parser.add_argument("--id", type=int, help="Task ID")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add" and args.task:
        manager.add_task(args.task)
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "complete" and args.id is not None:
        manager.complete_task(args.id)
    elif args.command == "delete" and args.id is not None:
        manager.delete_task(args.id)
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()