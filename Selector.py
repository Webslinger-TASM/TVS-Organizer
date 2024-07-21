import Utilites as Utils

import os
from typing import Tuple


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


def lister(extensions: tuple[str, ...], sub_extensions: tuple[str, ...]) -> Tuple[list[str], list[str]]:
    def sub_recursive(folder: str) -> None:
        sub_contents = [os.path.join(folder, content) for content in os.listdir(folder)]

        for sub_content in sub_contents:
            if os.path.isdir(sub_content):
                sub_recursive(sub_content)
            elif sub_content.endswith(extensions) or sub_content.endswith(sub_extensions):
                os.rename(sub_content, os.path.join(directory, os.path.basename(sub_content)))

    try:
        print("\nIf you want to use the current directory, leave it empty.")
        directory = input("What directory you want to use: ")

        if not directory:
            directory = os.getcwd()
    except OSError:
        print("Error: This is not a valid directory.")

    if input("\nSub-Recursive search? ") in ('y', "yes"):
        folders = [os.path.join(directory, content) for content in os.listdir(directory) if os.path.isdir(os.path.join(directory, content))]

        for folder in folders:
            sub_recursive(folder)

    os.chdir(directory)
    contents = os.listdir(directory)

    return ([content for content in contents if os.path.isfile(os.path.join(directory, content)) and content.endswith(extensions)],
            [content for content in contents if os.path.isfile(os.path.join(directory, content)) and content.endswith(sub_extensions)])


def main() -> Tuple[list[str], list[list[str]], tuple[str, ...]]:
    extensions, sub_extensions = ext()
    files, sub_files = lister(extensions, sub_extensions)

    return files, Utils.split_strings(sub_files, False, len(sub_extensions)), sub_extensions