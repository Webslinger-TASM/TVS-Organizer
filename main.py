import Selector
import Builder
import Sorter


def main():
    mode = input("How would you like to get the data from? (IMDb, Files, Writing) (1/2/3) ").lower()

    files, sub_files, sub_extensions = Selector.selector()
    new_filenames = Builder.ToFormat(mode, files)
    Sorter.sort(new_filenames, files, sub_files, sub_extensions)


if __name__ == "__main__":
    main()