from functions.note_file import note_file
from functions.todo import todo_check
from functions.settings import set_settings
from functions.view import find_file, view_td
import subprocess
import os
import json
import sys

def term(path:str, e:str):
    """A function that runs some terminal commands
    changes to the notes folder, and opens the note

    Args:
        path (str): path of the note
        e (str): editor to open 
        
    """
    folder = os.path.expanduser("~/Documents/Notes")
    os.chdir(folder)
    subprocess.run([e, path])


def settings() -> list:
    """
    Opens the settings.json file and checks what editor to run and if if should run git.

    Returns
    [editor, git]
    editor: str -> the editor to run
    git: bool -> if it should run git
    """
    with open("settings.json", "r") as f:
        content = f.read()
        content = json.loads(content)
        editor = content["editor"]
        git = content["git"]
    return [editor, git]


def run(e: str, g: bool):
    """
    The main function.
    It runs when main.py runs with no arguments

    e: str -> editor to open
    g: bool -> if it should run git
    """
    path = note_file()
    term(path, e)
    if g:
        git()


def todo(e: str, g: bool):
    """
    The todo function
    It runs when main.py runs with the -t argument

    e: str -> editor to open
    g: bool -> if it should run git
    """
    path = os.path.expanduser("~/Documents/Notes/todo.md")
    todo_check()

    with open(path, "a") as f:
        f.write("\n[ ] ")
    term(path, e)
    if g:
        git()


def c(g: bool):
    """
    The copy/paste function
    It runs when main.py runs with the -c argument

    g: bool -> if it should run git
    """
    try:
        import pyperclip
        s = pyperclip.paste()
        note_file(s)
    except ImportError:
        print("Error, Module Pyperclip is required\n Use 'pip install pyperclip'")


def git():
    """
    The git function
    """
    notes_path = os.path.expanduser("~/Documents/Notes")
    os.chdir(notes_path)
    os.system("git add .")
    os.system("git commit -m 'note'")
    os.system("git push -u origin main")


if __name__ == "__main__":
    sets = settings()
    e = sets[0]
    g = sets[1]
    arg = sys.argv
    if len(arg) == 1:
        run(e, g)
    elif len(arg) == 2:
        if arg[1] == "-t":
            todo(e, g)
        elif arg[1] == "-c":
            c(g)
        elif arg[1] == "-s":
            set_settings()
        elif arg[1] == "-v":
            find_file()
        elif arg[1] == "-vt":
            view_td()
    elif len(arg) == 3:
        if arg[1] == "-v":
            find_file(arg[2])
    else:
        print("Help\n  No arguments: Open the note for the day.\n  -c: Paste your clipboard on the note for the day\n  -t: Open the todo note.\n  -s: Settings.\n  -v: View the note for the day in the browser.\n  -v day/month/year: View the chosen note in the browser.\n")
