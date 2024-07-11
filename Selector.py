import os


# A function that returns files only from a list
def lister():
    files = []
    print("\nIf you want to use the current directory, leave it empty.")

    # Gets directory
    try:
        directory = input("What directory you want to use: ")

        if directory == "":
            directory = os.getcwd()

        os.chdir(directory)
    except OSError:
        print("Error, this is not a valid directory.")

    contents = os.listdir(directory)

    # Appends files only to the list
    for content in contents:
        if os.path.isfile(content):
            files.append(content)

    return files


# A function that filters files by their extension
def ext():
    extensions = []
    sub_extensions = []
    print("\nLeave empty if you finished.")

    # A loop to enter extensions
    while True:
        extension = input("Enter an extension: ").lower()
        if extension and extension[0] != '.':
            extension = '.' + extension

        elif extensions and not extension:
            sub_extension = input("Enter a sub extension: ").lower()
            if sub_extension:
                if sub_extension != '.':
                    sub_extension = '.' + extension

                sub_extensions.append(sub_extension)

            elif not sub_extension and not extension:
                break

        elif not extensions and not extension:
            print("No extensions has been entered.")
            exit()

        extensions.append(extension)

    return tuple(extensions), tuple(sub_extensions)


# Filters which files to edit and returns it
def selector():
    files = lister()
    extensions, sub_extensions = ext()
    selected_files, subtitle_files = [], []

    for file in files:
        if file.endswith(sub_extensions):
            subtitle_files.append(file)

        elif file.endswith(extensions):
            selected_files.append(file)

    return selected_files, subtitle_files