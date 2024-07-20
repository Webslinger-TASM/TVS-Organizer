from re import sub


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