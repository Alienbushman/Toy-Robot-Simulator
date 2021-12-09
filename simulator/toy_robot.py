"""
The toy robot class which is responsible for tracking the position of the toy robot on the board
"""
from simulator.direction import get_axis_mapping, get_direction, get_number_directions
from simulator.valid_position import is_valid_position


class ToyRobot:
    """
    The Toy robot class which tracks the x and y coordinates as wll as the direction
    """

    def __init__(self, x_coordinate: int, y_coordinate: int, direction: int):
        """
        :param x_coordinate: The x coordinate of the robot
        :param y_coordinate: They y coordinate of the robot
        :param direction: The direction which the robot is facing
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction

    def rotate_left(self):
        """
        Rotate the direction of the robot anti-clockwise
        :return: changes the direction of the robot
        """
        self.direction = (self.direction - 1) % get_number_directions()

    def rotate_right(self):
        """
        Rotate the direction of the robot clockwise
        :return: changes the direction of the robot
        """
        self.direction = (self.direction + 1) % get_number_directions()

    def move(self):
        """
        Moves the robot forward one space in the direction it is facing
        :return: changes the position of the robot
        """
        add_x_coordinate, add_y_coordinate = get_axis_mapping(self.direction)
        new_x_coordinate = self.x_coordinate + add_x_coordinate
        new_y_coordinate = self.y_coordinate + add_y_coordinate
        if is_valid_position(new_x_coordinate, new_y_coordinate):
            self.x_coordinate = new_x_coordinate
            self.y_coordinate = new_y_coordinate

    def get_location(self):
        """
        Returns the current location and direction the robot is facing
        :return: The current location and direction of the robot
        """
        return (
            str(self.x_coordinate)
            + ","
            + str(self.y_coordinate)
            + ","
            + get_direction(self.direction)
        )
