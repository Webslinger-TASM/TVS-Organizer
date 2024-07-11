import os


class ToFormat:
    def __init__(self, mode, files, name='', year='', sxxexxes='', _ep_total=0, ep_names='', extensions=''):
        self.mode = mode
        self.files = files
        self.name = self.get_name()
        self.year = self.get_year()
        self.sxxexxes, self._ep_total = self.get_sxxexxes()
        self.ep_names = self.get_ep_names()
        self.extensions = self.get_extensions()

    # Gets name
    @staticmethod
    def get_name():
        return input("\nShow name: ")

    # Gets year
    @staticmethod
    def get_year():
        year = ''
        year_start = input("What year did it started? ")
        year_end = input("What year did it ended? (Leave empty if there isn't) ")

        try:
            int(year_start)
            year = '(' + year_start

            if year_end:
                int(year_end)
                year += '-' + year_end + ')'
            else:
                year += ')'

        except ValueError:
            print(f"ValueError: {year_start} and/or {year_end} are/is not a valid number.")

        return year

    # Gets season and episode number for each episode
    def get_sxxexxes(self):
        ep_total = 0
        sxxexxes = []

        if input("\nIs it multiple seasons? (y/n) ") in ('y', 'yes'):
            se_nums = int(input("Number of seasons: "))
        else:
            se_nums = 1

        se_current = 1

        while se_current <= se_nums:
            if se_current < 10:
                se = 'S0' + str(se_current)
            else:
                se = 'S' + str(se_current)

            ep_num = int(input(f"Number of episodes at season {se_current}: "))
            ep_total += ep_num

            ep_current = 1
            se_current += 1

            while ep_current <= ep_num:
                if ep_current < 10:
                    ep = 'E0' + str(ep_current)
                else:
                    ep = 'E' + str(ep_current)

                if self.mode == 1:
                    sxxexxes.append(se + ep)
                else:
                    sxxexxes.append(se + ' ' + ep)

                ep_current += 1

        if ep_total != len(self.files):
            print(f"Error: The number of episode names has been created is {ep_total}, "
                  f"while the number of files are {len(self.files)}.")
            exit()

        return sxxexxes, ep_total

    # Gets episode's name
    def get_ep_names(self):
        ep_names = []

        # If there's a txt file shares the same name of the show, reads it.
        # It works by reading each line, and each line represents the episode name.
        if os.path.exists(f'{self.name}.txt'):
            with open(f'{self.name}.txt', 'r') as file:
                try:
                    lines = file.readlines()
                    if len(lines) != self._ep_total:
                        print(f"Error: Lines in '{file.name}' does not match the number of the episodes.")
                    else:
                        # Reads the file to add the episode's name
                        for line in lines:
                            if self.mode == 2:
                                line = '(' + line.strip() + ')'

                            ep_names.append(line.strip())

                except OSError:
                    print(f"Error: The file {file.name} is corrupted.")

        # If it doesn't exist, asks the user and appends it to the list
        else:
            ep_current = 1

            while len(ep_names) != self._ep_total:
                ep_name = input(f"Enter the name of episode {ep_current}: ")
                if self.mode == 2:
                    ep_name = '(' + ep_name + ')'

                ep_names.append(ep_name)
                ep_current += 1

        return ep_names

    # Gets extension files
    def get_extensions(self):
        extensions = []
        for file in self.files:
            extensions.append(os.path.splitext(file)[-1])

        return extensions
