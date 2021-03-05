from functions.note_file import note_file
from functions.todo import todo_check
from functions.settings import set_settings
from functions.view import find_file, view_td
from functions.nonday import nonday
from functions.paste import p, paste_file
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
    folder = b + "Notes/"
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
    with open("./.config/settings.json", "r") as f:
        content = f.read()
        content = json.loads(content)
        editor = content["editor"]
        git = content["git"]
        base = content["base"]
    return [editor, git, base]


def run(e: str, g: bool, b:str):
    """
    The main function.
    It runs when main.py runs with no arguments

    e: str -> editor to open
    g: bool -> if it should run git
    """
    path = note_file(b)
    term(path, e)
    if g:
        git(b)

def nonday_run(name: str, e:str, g:bool, b:str):
    path = nonday(b, name)
    term(path, e)
    if g:
        git(b)

def todo(e: str, g: bool, b:str):
    """
    The todo function
    It runs when main.py runs with the -t argument

    e: str -> editor to open
    g: bool -> if it should run git
    """
    path = b + "Notes/todo.md"
    todo_check(b)

    with open(path, "a") as f:
        f.write("\n- [] ")
    term(path, e)
    if g:
        git(b)





def git(b:str):
    """
    The git function
    """
    notes_path = b
    os.chdir(notes_path)
    os.system("git add .")
    os.system("git commit -m 'note'")
    os.system("git push -u origin main")


if __name__ == "__main__":
    if os.path.exists("./.config/settings.json"):
        sets = settings()
        e = sets[0]
        g = sets[1]
        b = sets[2]
    else:
        e = "nvim"
        g = False
        b = "/home/force/Documents/"
    arg = sys.argv
    if len(arg) == 1:
        run(e, g, b)
    elif len(arg) == 2:
        if arg[1] == "-t":
            todo(e, g, b)
        elif arg[1] == "-p":
            p(g, b, note_file)
        elif arg[1] == "-s":
            set_settings()
        elif arg[1] == "-v":
            find_file(b)
        elif arg[1] == "-vt":
            view_td(b)
        else:
            nonday_run(arg[1], e, g, b)
            
    elif len(arg) == 3:
        if arg[1] == "-v":
            find_file(b, arg[2])
        elif arg[1] == "-p":
            paste_file(b, arg[2])
    else:
        print("Help\n  No arguments: Open the note for the day.\n  -c: Paste your clipboard on the note for the day\n  -t: Open the todo note.\n  -s: Settings.\n  -v: View the note for the day in the browser.\n  -v day/month/year: View the chosen note in the browser.\n")
