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


def split_by_extensions(old_list: list[str], extensions: tuple[str, ...]) -> list[list[str]]:
    new_list: list[list[str]] = []

    index = 0

    while index != len(old_list):
        new_list.append(old_list[index:index + len(extensions)])

        index += len(extensions)

    return new_list


def selector() -> Tuple[list[str], list[list[str]], tuple[str, ...]]:
    print("\nWarning: Files will be sorted alphabetically.")
    
    files = lister()
    extensions, sub_extensions = ext()    

    selected_files = [file for file in files if file.endswith(extensions)]
    sub_files = [file for file in files if file.endswith(sub_extensions)]
    splitted_sub_files = split_by_extensions(sub_files, sub_extensions)

    return selected_files, splitted_sub_files, sub_extensions
