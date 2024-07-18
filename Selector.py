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

    return tuple(extensions), tuple(sub_extensions)


def selector() -> Tuple[list[str], list[str], tuple[str, ...]]:
    files = lister()
    extensions, sub_extensions = ext()

    selected_files = [file for file in files if file.endswith(extensions)]
    sub_files = [file for file in files if file.endswith(sub_extensions)]

    return selected_files, sub_files, sub_extensions