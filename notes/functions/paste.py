import os
from functions.note_file import note_file
from functions.day import get_date

def paste_file(b: str, name: str = ""):
    name = name.strip()
    if name[0] == "-":
        n_date(b,name)
    else:
        date(b, name)


def n_date(b:str, name:str):
    name = name[1:]
    pa = b + f"Notes/note/{name}.md"
    if os.path.exists(pa):
        paste(pa)
    else:
        print("Sorry! That file does not exist.\n\n    -name\n")

def date(b:str, name:str):
    if name:
        day_list = name.split("/")
    else:
        day_list = get_date(False)

    pa = b + f"Notes/{day_list[2]}/{int(day_list[1])}/{int(day_list[0])}.md"
    if os.path.exists(pa):
        paste(pa)
    else:
        print("Sorry! That file does not exist.\n\n    day/month/year\n")



def p(g: bool, b:str, fun):
    """
    The copy/paste function
    It runs when main.py runs with the -c argument

    g: bool -> if it should run git
    b: str -> base folder
    """
    try:
        import pyperclip
        s = pyperclip.paste()
        fun(b, s)
    except ImportError:
        print("Error, Module Pyperclip is required\n Use 'pip install pyperclip'")


def paste(pa: str):
    try:
        import pyperclip
        s = pyperclip.paste()
        with open(pa, "a") as f:
            f.write("\n\n"+s)
    except ImportError:
        print("Error, Module Pyperclip is required\n Use 'pip install pyperclip'")