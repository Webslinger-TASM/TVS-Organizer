import os
import Builder


# Get user preferences about naming files/folders
def settings(new_filename):
    se_addon_name = ''
    se_addon_year = ''
    ep_addon_name = ''
    ep_addon_year = ''

    if input("\nShow name in each season? (y/n) ") in ('y', 'yes'):
        se_addon_name = new_filename.name
    if input("Year in each season? (y/n) ") in ('y', 'yes'):
        se_addon_year = new_filename.year

    if input("Show name in each episode? (y/n) ") in ('y', 'yes'):
        ep_addon_name = new_filename.name + ' '
        if input("Year in each episode? (y/n) ") in ('y', 'yes'):
            ep_addon_year = new_filename.year + ' '

    return [se_addon_name, se_addon_year, ep_addon_name, ep_addon_year]


# Creates folders and moves files into them
def sort(new_filenames, files, sub_files):
    addons = settings(new_filenames)

    # Check for the last element and S(1)1
    if new_filenames.sxxexxes[-1][1] != '0':
        se_total = int(new_filenames.sxxexxes[-1][1])
    # If not then S0(1)
    else:
        se_total = int(new_filenames.sxxexxes[-1][2])

    # Get files location and create a folder for the show
    files_dir = os.getcwd()
    show_dir = os.path.join(files_dir, os.path.basename(new_filenames.name + ' ' + new_filenames.year)).strip()
    os.makedirs(show_dir, exist_ok=True)

    se_current = 1

    while se_current <= se_total:
        if se_current < 10:
            se = '0' + str(se_current)
        else:
            se = str(se_current)

        if addons[1]:
            print(f"\nFor season {se_current}:")
            addons[1] = Builder.ToFormat.get_year()

        if addons[3]:
            if addons[1]:
                addons[3] = addons[1]
            else:
                print(f"\nFor season {se_current}:")
                addons[3] = Builder.ToFormat.get_year()

        # Spider-Man (1994) - Season 1 or Spider-Man (1994) Season 1
        if addons[0]:
            if new_filenames.mode == 1:
                se_dir = os.path.join(show_dir, addons[0] + addons[1] + ' - ' + 'Season ' + str(se_current)).strip()
            else:
                se_dir = os.path.join(show_dir, addons[0] + addons[1] + ' ' + 'Season ' + str(se_current)).strip()

        # Season 1 - (1994)
        elif addons[1]:
            se_dir = os.path.join(show_dir, 'Season ' + se + ' ' + addons[1]).strip()
        # Season 1
        else:
            se_dir = os.path.join(show_dir, 'Season ' + se).strip()

        # Create season folder inside the show folder and enter it
        os.chdir(show_dir)
        os.makedirs(se_dir, exist_ok=True)
        os.chdir(se_dir)

        # Create episode folders, renames files, moves files
        for file, sxxexx, ep_name, ext in zip(files, new_filenames.sxxexxes, new_filenames.ep_names, new_filenames.extensions):
            if int(sxxexx[1]) == se_current or int(sxxexx[2]) == se_current:
                # Creates a folder for the episode
                if new_filenames.mode == 1:
                    ep_dir = os.path.join(se_dir, addons[2] + addons[3] + sxxexx + ' - ' + ep_name).strip()
                else:
                    ep_dir = os.path.join(se_dir, addons[2] + addons[3] + sxxexx + ' ' + ep_name).strip()

                os.makedirs(ep_dir, exist_ok=True)

                # Moves and renames the file into the episode folder
                new_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + ext).strip()
                os.rename(os.path.join(files_dir, file), new_filename)

                # Does the same as to the previous file if there's subtitle files
                if sub_files:
                    new_sub_filename = os.path.join(ep_dir, os.path.basename(ep_dir) + '.srt').strip()
                    os.rename(os.path.join(files_dir, sub_files[0]), new_sub_filename)
                    sub_files.remove(sub_files[0])

        se_current += 1