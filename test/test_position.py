""""
Test the internal logic for the ToyRobot class
"""
from unittest import TestCase

from simulator.toy_robot import ToyRobot


class TestPosition(TestCase):
    """"
    The test cases for the ToyRobots class
    """
    def test_instantiation_success(self):
        """"
        Validate instantiation
        """
        position = ToyRobot(2, 1, 0)
        self.assertEqual(type(position), ToyRobot)
        self.assertEqual(position.x_coordinate, 2)
        self.assertEqual(position.y_coordinate, 1)
        self.assertEqual(position.direction, 0)

    def test_basic_rotate_left(self):
        """"
        Validate left rotation
        """
        position = ToyRobot(2, 1, 1)
        position.rotate_left()
        self.assertEqual(position.direction, 0)

    def test_edge_rotate_left(self):
        """"
        Validate left rotation edge case
        """
        position = ToyRobot(2, 1, 0)
        position.rotate_left()
        self.assertEqual(position.direction, 3)

    def test_basic_rotate_right(self):
        """"
        Validate right rotation
        """
        position = ToyRobot(2, 1, 0)
        position.rotate_right()
        self.assertEqual(position.direction, 1)

    def test_edge_rotate_right(self):
        """"
        Validate right rotation edge case
        """
        position = ToyRobot(2, 1, 3)
        position.rotate_right()
        self.assertEqual(position.direction, 0)

    def test_basic_move(self):
        """"
        Validate a basic movement
        """
        position = ToyRobot(0, 0, 0)
        position.move()
        self.assertEqual(position.x_coordinate, 0)
        self.assertEqual(position.y_coordinate, 1)

    def test_move_along_edge(self):
        """"
        Validate moving around the edges of a square
        """
        position = ToyRobot(0, 0, 0)
        for _ in range(5):
            position.move()
        self.assertEqual(position.x_coordinate, 0)
        self.assertEqual(position.y_coordinate, 4)
        position.rotate_right()
        for _ in range(4):
            position.move()
        self.assertEqual(position.x_coordinate, 4)
        self.assertEqual(position.y_coordinate, 4)
        position.rotate_right()
        for _ in range(4):
            position.move()
        self.assertEqual(position.x_coordinate, 4)
        self.assertEqual(position.y_coordinate, 0)
        position.rotate_right()
        for _ in range(5):
            position.move()
        self.assertEqual(position.x_coordinate, 0)
        self.assertEqual(position.y_coordinate, 0)
