import Selector
import Builder
import Sorter


def main():
    files, sub_files = Selector.selector()
    
    if input("\nHow would you like to rename your files? (Spider/Bat) (1/2) ").lower() in ('1', 'spider'):
        mode = 1
    else:
        mode = 2

    new_filenames = Builder.ToFormat(mode, files)
    Sorter.sort(new_filenames, files, sub_files)
    input("\n\n\nPress the Enter button to exit.")


if __name__ == "__main__":
    main()