import random
from datetime import date

my_list = [1, 2, 3, 4]


def get_last_shuffle_date():
    try:
        with open("last_shuffle_date.txt", "r") as file:
            last_shuffle_date_str = file.read()
            return date.fromisoformat(last_shuffle_date_str)
    except FileNotFoundError:
        return None
    except ValueError:
        return None


def set_last_shuffle_date(last_shuffle_date):
    with open("last_shuffle_date.txt", "w") as file:
        file.write(last_shuffle_date.isoformat())


def read_last_shuffle_list():
    try:
        with open("last_shuffle_list.txt", "r") as file:
            last_shuffle_list_str = file.read()
            inner_last_shuffle_list = last_shuffle_list_str.split('\n')
            return inner_last_shuffle_list
    except FileNotFoundError:
        return []


last_shuffle_list = read_last_shuffle_list()


def shuffle_list():
    last_shuffle_date = get_last_shuffle_date()
    current_date = date.today()

    if last_shuffle_date and last_shuffle_date == current_date:
        print("Current:", current_date)
        print("Last:", last_shuffle_date)
        print("Same: ", last_shuffle_list)
    else:
        random.shuffle(my_list)
        random_list = my_list.copy()

        set_last_shuffle_date(current_date)

        with open("last_shuffle_list.txt", "w") as file:
            file.write('\n'.join(map(str, random_list)))

        print("Current:", current_date)
        print("Last:", current_date)
        print("Random:", random_list)


shuffle_list()
