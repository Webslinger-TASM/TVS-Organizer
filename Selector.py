import Utilites as Utils

import os
from typing import Tuple


def lister() -> list[str]:
    try:
        print("\nIf you want to use the current directory, leave it empty.")
        directory = input("What directory you want to use: ")

        if directory == "":
            directory = os.getcwd()

        os.chdir(directory)
    except OSError:
        print("Error: This is not a valid directory.")

    contents = os.listdir(directory)
    files = [content for content in contents if os.path.isfile(content)]

    return files


def ext() -> Tuple[tuple[str, ...], tuple[str, ...]]:
    extensions: list[str] = []
    sub_extensions: list[str] = []

    print("\nLeave empty if you finished.")
    while True:
        extension = input("Enter an extension: ").lower()

        if extension:
            extensions.append(extension)
        elif extensions:
            while True:
                sub_extension = input("Enter a sub extension: ").lower()

                if sub_extension:
                    sub_extensions.append(sub_extension)
                else:
                    break
            break
        else:
            raise Exception("Error: No extensions has been entered.")

    return tuple(sorted(extensions)), tuple(sorted(sub_extensions))


def selector() -> Tuple[list[str], list[list[str]], tuple[str, ...]]:
    print("\nWarning: Files should be sorted alphabetically.")
    
    files = lister()
    extensions, sub_extensions = ext()    

    selected_files = [file for file in files if file.endswith(extensions)]
    sub_files = [file for file in files if file.endswith(sub_extensions)]

    return selected_files, Utils.split_strings(sub_files, False, len(sub_extensions)), sub_extensions
