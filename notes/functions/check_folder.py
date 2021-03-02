import os
import functions.day as day


def check():
    """
    Check if the notes folder exists
    """
    # check if notes folder exists
    folder = os.path.expanduser('~/Documents/Notes')
    make_d(folder)

    # get date
    date = day.get_date(False)

    # check if year folder exists
    folder = os.path.expanduser('~/Documents/Notes/' + str(int(date[2])))
    make_d(folder)

    # check if month folder exists
    folder = os.path.expanduser('~/Documents/Notes/' + str(int(date[2])) + "/" + str(int(date[1])))
    make_d(folder)

    return folder


def make_d(folder: str):
    """Check if a folder exists, if not then create it

    Args:
        folder (str): the folder to check
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
