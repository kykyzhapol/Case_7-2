from const import *
from ru_local import *


def get_color_choice() -> str:
    """
    The function asks the user for two colors and generates a list of them
    :return: color_list
    """
    print(COLOR_TITLE)

    while True:
        try:
            color_index = int(input(COLOR_INPUT))
            try:
                colort = COLOR[color_index - 1]
                break
            except IndexError:
                print(COLOR_ERROR)
        except ValueError:
            print(COLOR_ERROR)

    return colort
