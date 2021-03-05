import json
import os


def set_settings():
    with open("./.config/settings.json", "r") as f:
        data = json.load(f)

        e = input(f"Editor: ")
        g = input(f"Execute git (y/n): ")
        b = input(f"Base Folder: ")

        if e:
            data["editor"] = e

        if g == "yes" or g == "y" or g == "Yes" or g == "Y":
            data["git"] = True
        else:
            data["git"] = False
        
        if b:
            data["base"] = b

    os.remove("./.config/settings.json")
    with open("./.config/settings.json", "w") as f:
        json.dump(data, f, indent=4)
