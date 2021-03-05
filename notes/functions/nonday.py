import os
import functions.check_folder as check_folder

def nonday(b: str, name: str) -> str:
    name = name.strip()
    if name[0] == "-":
        name = name[1:]
    name = name.replace(" ", "-")
    exists = check_nonday(b, name)
    if exists:
        return b + "Notes/note/" + name +".md"
    else:
        if os.path.exists("./.config/templates/non_date_template.md"):
            with open("./.config/templates/non_date_template.md", "r") as t:
                template = "\n" + t.read() + "\n"
        else:
            template = ""
        with open(b + "Notes/note/" + name +".md", "w") as f:
            f.write("# " + name.upper() + "\n")
            f.write(template)
        return b + "Notes/note/" + name +".md"

def check_nonday(b: str, name:str) -> bool:
    folder = b + "Notes/"
    check_folder.make_d(folder)

    folder = folder + "note/"
    check_folder.make_d(folder)

    folder = folder + name + ".md"
    if os.path.exists(folder):
        return True
    else:
        return False


#print(nonday("/home/force/Documents/", "   -df  daf adf "))

