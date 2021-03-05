import markdown
import tempfile
import webbrowser
from functions.day import get_date
import os


def find_file(b: str, name: str = ""):
    name = name.strip()
    if name:
        if name[0] == "-":
            n_date(b,name)
        else:
            date(b, name)
    else:
        date(b, name)


def n_date(b:str, name:str):
    name = name[1:]
    pa = b + f"Notes/note/{name}.md"
    if os.path.exists(pa):
        to_html(pa)
    else:
        print("Sorry! That file does not exist.\n\n    -name\n")

def date(b:str, name:str):
    if name:
        day_list = name.split("/")
    else:
        day_list = get_date(False)

    pa = b + f"Notes/{day_list[2]}/{int(day_list[1])}/{int(day_list[0])}.md"
    if os.path.exists(pa):
        to_html(pa)
    else:
        print("Sorry! That file does not exist.\n\n    day/month/year\n")


def view_td(b):
    pa = b + "Notes/todo.md"
    if os.path.exists(pa):
        to_html(pa)
    else:
        print("Sorry! You don't have a Todo file.\n")


def to_html(file):
    with open(file, "r") as f:
        md = f.read()
        html = markdown.markdown(md, extensions=['tables', 'footnotes'])

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        url = "file:///" + f.name
        f.write(html)
    webbrowser.open(url)
