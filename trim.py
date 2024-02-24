import os

def remove_strings_from_title(name):
    remove_strings = os.getenv("REMOVE_STRINGS").split(",")
    for remove_string in remove_strings:
        name = name.replace(remove_string, "")
    return name