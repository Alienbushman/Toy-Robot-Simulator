"""
Checks for whether a board position is valid
"""
MAX_ROW = 5
MAX_COLUMN = 5


def is_valid_position(x_coordinate, y_coordinate):
    """
    Checks whether the board position is valid
    :param x_coordinate: The x coordinate
    :param y_coordinate:  The y coordinate
    :return: A boolean whether the board position is valid
    """
    if x_coordinate >= MAX_COLUMN:
        return False
    elif x_coordinate < 0:
        return False
    elif y_coordinate >= MAX_ROW:
        return False
    elif y_coordinate < 0:
        return False
    return True
