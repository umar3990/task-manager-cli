## File: README.md
# TaskCLI - Simple Python Task Manager

A command-line based task manager built with basic Python to showcase understanding of:
- Python CLI development (`argparse`)
- JSON storage
- Modular structure

## Features
- Add, list, complete, and delete tasks
- Persistent JSON-based storage
- Clean, modular code

## Setup & Usage

```bash
# Clone the repo

$ cd taskcli-python

# Run commands
$ python main.py add --task "Buy groceries"
$ python main.py list
$ python main.py complete --id 1
$ python main.py delete --id 1
```

## Example Output
```bash
$ python main.py add --task "Write blog post"
Task added: Write blog post

$ python main.py list
[✗] 1: Write blog post

$ python main.py complete --id 1
Task 1 marked as complete.

$ python main.py delete --id 1
Task 1 deleted.
