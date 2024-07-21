from re import sub, match
from typing import Tuple


def clean_string(string: str, mode) -> str:
    clean_string = sub(r'[\\/|]', '_', string)
    clean_string = sub('[*?]', '', clean_string)
    clean_string = sub('"', "'", clean_string)
    clean_string = sub('<', '(', clean_string)
    clean_string = sub('>', ')', clean_string)

    if mode in ("spider", '1'):
        clean_string = sub(':', ' -', clean_string)
    else:
        clean_string = sub(':', ';', clean_string)

    return clean_string


def split_strings(old_list: list[str], num_of_lists: int or bool, num_of_strings: list[int] or int) -> list[list[str]]:
    new_list: list[list[str]] = []

    index = 0

    if num_of_lists:
        for list_num in range(num_of_lists):
            new_list.append(old_list[index:index + num_of_strings[list_num]])

            index += num_of_strings[list_num]
    else:
        while index != len(old_list):
            new_list.append(old_list[index:index + num_of_strings])

            index += num_of_strings

    return new_list


def sort_titles(titles: list[str], mode) -> Tuple[list[str], list[str]]:
    sxxexxes: list[str] = []
    ep_names: list[str] = []

    for title in titles:
        sxxexx = match(r"S(\d+)\.E?(\d+)?", title)
        sxx = f"S{int(sxxexx.group(1)):02d}"
        exx = f"E{int(sxxexx.group(2)):02d}"

        sxxexxes.append(f"{sxx}{exx}")

        index = len(f"{sxx+exx} _")
        ep_names.append(clean_string(title[index:], mode))

    return sxxexxes, ep_names


def sort_dates(first_date: str, last_date: str) -> str:
    if first_date[-4:] != last_date[-4:]:
        return f"({first_date[-4:]}-{last_date[-4:]})"
    else:
        return f"({first_date[-4:]})"


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