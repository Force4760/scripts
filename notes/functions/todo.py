import os


def todo_check():
    """
    Check if todo file exists
    """
    file = os.path.expanduser("~/Documents/Notes/todo.md")
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("# TODO")
