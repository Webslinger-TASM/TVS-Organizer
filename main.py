import Selector
import Builder
import Sorter


def main():
    source = input("How would you like to get the data from? (IMDb, Files, Writing) (1/2/3) ").lower()
    mode = input("How would you like to sort/rename your files? (Spider/Bat) (1/2) ")

    files, sub_files, sub_extensions = Selector.selector()
    new_filenames = Builder.ToFormat(source, mode, files)
    Sorter.sort(new_filenames, sub_files, sub_extensions, mode)


if __name__ == "__main__":
    main()