import Builder
import Utilites as Utils

import os
from tqdm import tqdm
from typing import List, Union


def settings(name) -> List[Union[str, bool]]:
    se_addon_name = ''
    se_addon_year = False
    ep_addon_name = ''
    ep_addon_year = False

    if input("\nShow name in each season? (y/n) ") in ('y', 'yes'):
        se_addon_name = name
    if input("Year in each season? (y/n) ") in ('y', 'yes'):
        se_addon_year = True

    if input("Show name in each episode? (y/n) ") in ('y', 'yes'):
        ep_addon_name = name
        if input("Year in each episode? (y/n) ") in ('y', 'yes'):
            ep_addon_year = True

    return [se_addon_name, se_addon_year, ep_addon_name, ep_addon_year]


def main(new_filenames: Builder.ToFormat, sub_files: list[list[str]], sub_extensions: tuple[str, ...], mode) -> None:
    addons = settings(new_filenames.name)
    files_dir = os.getcwd()
    show_dir = os.path.join(files_dir, os.path.basename(new_filenames.name + " " + Utils.get_year_range(new_filenames.years))).strip()
    os.makedirs(show_dir, exist_ok=True)

    index = 0

    for se_current in tqdm(range(new_filenames.se_total)):

        addons[1] = f"{new_filenames.years[se_current]} " if addons[1] else ''
        addons[3] = f"{new_filenames.years[se_current]} " if addons[3] else ''

        # Spider-Man (1994) - Season 01 or Season 01 (1994)
        if addons[0]:
            se_dir = os.path.join(show_dir, f"{addons[0]} {addons[1]}" + "- " + f"Season {se_current+1:02d}").strip()
        else:
            se_dir = os.path.join(show_dir, "Season " + f"{se_current+1:02d} " + addons[1]).strip()

        os.chdir(show_dir)
        os.makedirs(se_dir, exist_ok=True)
        os.chdir(se_dir)

        for file, sxxexx, ep_name, ext in zip(new_filenames.files[se_current], new_filenames.sxxexxes[se_current], new_filenames.ep_names[se_current], new_filenames.extensions[se_current]):
            if mode in ("spider", '1'):
                if addons[2]:
                    ep_dir = os.path.join(se_dir, f"{addons[2]} {addons[3]}" + '- ' + sxxexx + " - " + ep_name).strip()
                else:
                    ep_dir = os.path.join(se_dir, sxxexx + " - " + ep_name).strip()
            else:
                if addons[2]:
                    ep_dir = os.path.join(se_dir, f"{addons[2]} {addons[3]}" + f"{sxxexx[0:3]} {sxxexx[3:]} " + f"({ep_name})").strip()
                else:
                    ep_dir = os.path.join(se_dir, f"{sxxexx[0:3]} {sxxexx[3:]} " + f"({ep_name})").strip()

            os.makedirs(ep_dir, exist_ok=True)
            new_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + ext).strip()
            os.rename(os.path.join(files_dir, file), new_filename)
            
            if sub_files and index <= len(sub_files):
                for sub_file, sub_ext in zip(sub_files[index], sub_extensions):
                    new_sub_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + os.path.splitext(sub_file)[-1]).strip()
                    os.rename(os.path.join(files_dir, sub_file), new_sub_filename)

            index += 1