import Utilites as Utils
import IMDb_Scraper as IMDb

import os
from typing import Tuple


class ToFormat:
    def __init__(self, source, mode, files):
        self.source = source
        self.mode = mode
        self.files = files
        self.name = self.get_name()

        if self.source in ("imdb", '1'):
            self.years, self.sxxexxes, self.se_total, self.ep_names = IMDb.main(self.mode)
            self.ep_total = [len(season) for season in self.sxxexxes]
        else:
            self.sxxexxes, self.se_total, self.ep_total = self.get_sxxexxes()
            self.years = self.get_years()
            self.ep_names = self.get_ep_names()

        self.extensions = self.get_extensions()
        self.files = Utils.split_strings(files, self.se_total, self.ep_total)

    def get_name(self) -> str:
        return Utils.clean_string(input("\nShow name: "), self.mode)

    def get_years(self) -> list[str]:
        years: list[str] = []

        for se_current in range(self.se_total):
            print(f"\nFor season {se_current+1}")
            try:
                year_start = int(input("What year did it started? "))
                year_end = input("What year did it ended? (Leave empty if there isn't) ")

                tmp_year = [f"({year_start}"]

                if year_end:
                    tmp_year.append(f"-{int(year_end)})")
                else:
                    tmp_year.append(')')

                years.append(''.join(tmp_year))

            except ValueError:
                print(f"ValueError: {year_start} and/or {year_end} are/is not a valid number.")

        return years

    def get_sxxexxes(self) -> Tuple[list[list[str]], int, list[int]]:
        ep_total: list[int] = []
        sxxexxes: list[list[str]] = []

        if input("\nIs it multiple seasons? (y/n) ") in ('y', 'yes'):
            try:
                se_total = int(input("Number of seasons: "))
            except ValueError:
                print(f"ValueError: {se_total} is not a valid number.")
        else:
            se_total = 1

        for se_current in range(se_total):
            se = f"S{se_current+1:02d}"

            try:
                ep_num = int(input(f"Number of episodes at season {se_current+1}: "))
                ep_total.append(ep_num)
            except ValueError:
                print(f"ValueError: {ep_num} is not a valid number.")

            tmp_sxxexxes: list[str] = []

            for ep_current in range(ep_total[se_current]):
                ep = f"E{ep_current+1:02d}"
                tmp_sxxexxes.append(f"{se}{ep}")

            sxxexxes.append(tmp_sxxexxes)

        if sum(ep_total) != len(self.files):
            raise Exception(f"Error: The number of episodes {sum(self.ep_total)} has been created"
                            f" doesn't match the number of files {len(self.files)}.")

        return sxxexxes, se_total, ep_total

    def get_ep_names(self) -> list[list[str]]:
        ep_names: list[list[str]] = []

        for se_current in range(self.se_total):
            if self.source in ("files", '2'):
                try:
                    with open(f"{input(f"TXT filename for season {se_current+1}: ")}.txt", 'r') as file:
                        lines = file.readlines()

                        if len(lines) != self.ep_total[se_current-1]:
                            raise Exception(f"Error: Lines in '{file.name}' does not match the number of the episodes.")

                        ep_names.append([Utils.clean_string(line.strip(), self.mode) for line in lines])

                except FileNotFoundError or OSError as err:
                    print(f"An error occured while trying to read the file {file.name}. {err}")

            else:
                tmp_ep_names: [list[str]] = []

                for ep_current in range(self.ep_total[se_current]):
                    tmp_ep_names.append(input(f"Enter the name of episode {ep_current+1} for season {se_current+1}: "))

                ep_names.append([Utils.clean_string(ep_name, self.mode) for ep_name in tmp_ep_names])

        return ep_names

    def get_extensions(self) -> list[list[str]]:
        return Utils.split_strings([os.path.splitext(file)[-1] for file in self.files], self.se_total, self.ep_total)