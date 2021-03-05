import os


def todo_check(b:str):
    """
    Check if todo file exists
    """
    file = b + "Notes/todo.md"
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("# TODO")
