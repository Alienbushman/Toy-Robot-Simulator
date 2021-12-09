"""The module that determines which are valid directions and the impact directions have on
positional movement """

# the direction to the mapping of the values
direction_value_mapping = {"NORTH": 0, "EAST": 1, "SOUTH": 2, "WEST": 3}
# the mapping of the directions to the values
value_direction_mapping = {
    value: key for (key, value) in direction_value_mapping.items()
}

# mapping the associated values to which coordinates in the x and y-axis needs to be updated when
# moving
value_axis_mapping = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


def get_valid_direction(direction: str):
    """
    Verifies that the direction is a valid parameter
    :param direction: The direction name
    :return: A boolean whether the direction is valid
    """

    return direction in direction_value_mapping


def get_number_directions():
    """
    A function to get the number of valid directions used for mathematical functions
    :return: The number of valid directions
    """
    return len(direction_value_mapping)


def get_position(direction: str):
    """
    A function which takes the direction in a string format and returns the associated numeric
    value, used to map from the direction to the internal mapping for the object ToyRobot :param
    direction: The parameter name, such as "NORTH, EAST, SOUTHm WEST" (consult
    direction_value_mapping for a full list) :return: The numeric value corresponding to the
    direction
    """
    return direction_value_mapping[direction]


def get_direction(value: int):
    """
    A function which takes the associated numeric value of the direction and returns direction in
    a string format, used to map from the internal mapping for the object ToyRobot to the
    direction :param value: The associated numeric value in the object ToyRobot :return: the
    direction in a string format
    """
    return value_direction_mapping[value]


def get_axis_mapping(value: int):
    """
    The functions which takes the internal mapping of the direction and maps it to the change in
    grid :param value: The numeric representation of the direction :return: x_coordinate,
    y_coordinate
    """
    tuple_mapping = value_axis_mapping[value]
    return tuple_mapping[0], tuple_mapping[1]
