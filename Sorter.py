import os
import Builder
from tqdm import tqdm
from typing import Tuple, List, Union


def settings(new_filename, mode) -> List[Union[str, bool]]:
    se_addon_name = ''
    se_addon_year = False
    ep_addon_name = ''
    ep_addon_year = False

    if input("\nShow name in each season? (y/n) ") in ('y', 'yes'):
        se_addon_name = new_filename.name
        se_addon_name += ' - ' if mode in ("spider", '1') else None
    if input("Year in each season? (y/n) ") in ('y', 'yes'):
        se_addon_year = True

    if input("Show name in each episode? (y/n) ") in ('y', 'yes'):
        ep_addon_name = new_filename.name
        if input("Year in each episode? (y/n) ") in ('y', 'yes'):
            ep_addon_year = True

    return [se_addon_name, se_addon_year, ep_addon_name, ep_addon_year]


def get_year_range(years: list[str]) -> str:
    if years[0] != years[-1]:
        stripped_first_season_year = years[0].strip("()")
        first_year = stripped_first_season_year.split('-')

        stripped_last_season_year = years[-1].strip("()")
        last_year = stripped_last_season_year.split('-')

        year = f"({first_year[0]}-{last_year[len(last_year)-1]})"
    else:
        year = years[0]

    return year


def split_strings(files: list, new_filenames) -> Tuple[list[list[str]], list[list[str]]]:
    new_files: list[list[str]] = []
    new_extensions: list[list[str]] = []

    index = 0
    
    for se_current in range(new_filenames.se_total):
        new_files.append(files[index:index+new_filenames.ep_total[se_current]])
        new_extensions.append(new_filenames.extensions[index:index+new_filenames.ep_total[se_current]])

        index += new_filenames.ep_total[se_current]

    return new_files, new_extensions


def sort(new_filenames: Builder.ToFormat, files: list[str], sub_files: list[str], sub_extensions: tuple[str, ...]) -> None:
    mode = input("\nHow would like to rename your files? (Spider/Bat) (1/2) ").lower()
    addons = settings(new_filenames, mode)
    files, new_filenames.extensions = split_strings(files, new_filenames)
    files_dir = os.getcwd()
    show_dir = os.path.join(files_dir, os.path.basename(new_filenames.name + " " + get_year_range(new_filenames.years)))
    os.makedirs(show_dir, exist_ok=True)

    for se_current in tqdm(range(new_filenames.se_total)):

        addons[1] = f"{new_filenames.years[se_current]} " if addons[1] else ''
        addons[3] = f"{new_filenames.years[se_current]} " if addons[3] else ''

        # Spider-Man (1994) - Season 01 or Season 01 (1994)
        if addons[0]:
            se_dir = os.path.join(show_dir, f"{addons[0]} {addons[1]}" + " - " + f"Season {se_current+1:02d}")
        else:
            se_dir = os.path.join(show_dir, "Season " + f"{se_current+1:02d} " + addons[1]).strip()

        os.chdir(show_dir)
        os.makedirs(se_dir, exist_ok=True)
        os.chdir(se_dir)

        for file, sxxexx, ep_name, ext in zip(files[se_current], new_filenames.sxxexxes[se_current], new_filenames.ep_names[se_current], new_filenames.extensions[se_current]):
            if mode in ("spider", '1'):
                ep_dir = os.path.join(se_dir, f"{addons[2]} {addons[3]}" + sxxexx + " - " + ep_name).strip()
            else:
                ep_dir = os.path.join(se_dir, f"{addons[2]} {addons[3]}" + sxxexx + " " + f"({ep_name})").strip()

            os.makedirs(ep_dir, exist_ok=True)
            new_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + ext)
            os.rename(os.path.join(files_dir, file), new_filename)

            for sub_file, sub_ext in zip(sub_files, sub_extensions):
                new_sub_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + os.path.splitext(sub_file)[-1])
                os.rename(os.path.join(files_dir, sub_file), new_sub_filename)
                sub_files.remove(sub_file)