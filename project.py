import json
import os
from datetime import datetime

# File to store tasks
TODO_FILE = "todo.json"


def load_tasks():
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def add_task(tasks, description):
    task = {
        "id": len(tasks["tasks"]) + 1,
        "description": description,
        "completed": False
    }
    tasks["tasks"].append(task)
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
    print(f"Added: '{description}'")


def main():

    tasks = load_tasks()
    print("To-Do List Manager (Type 'help' for commands)")  # Welcome message
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "help":
            print("\nCommands:")
            print("add <task> - Add a new task")
            print("list - Show all tasks")
            print("done <id> - Mark task as complete/incomplete")
            print("delete <id> - Delete a task")
            print("exit - Quit the program")
        
        elif command.startswith("add "):
            description = command[4:].strip()
            add_task(tasks, description)


        elif command == "exit":
            print("Saving tasks and exiting...")
            break
        
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
