import markdown
import tempfile
import webbrowser
from functions.day import get_date
import os


def find_file(day: str = ""):
    if day:
        day_list = day.split("/")
    else:
        day_list = get_date(False)

    p = f"~/Documents/Notes/{day_list[2]}/{day_list[1]}/{day_list[0]}.md"
    pa = os.path.expanduser(p)
    if os.path.exists(pa):
        to_html(pa)
    else:
        print("Sorry! That file does not exist.\n\n    day/month/year\n")


def view_td():
    p = "~/Documents/Notes/todo.md"
    pa = os.path.expanduser(p)
    if os.path.exists(pa):
        to_html(pa)
    else:
        print("Sorry! You don't have a Todo file.\n")


def to_html(file):
    with open(file, "r") as f:
        md = f.read()
        html = markdown.markdown(md)

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        url = "file:///" + f.name
        f.write(html)
    webbrowser.open(url)
