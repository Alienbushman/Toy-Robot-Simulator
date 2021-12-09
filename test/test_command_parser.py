""""
Test how the robot moves
"""
from unittest import TestCase

from simulator.command_parser import parse_text


class Test(TestCase):
    """"
    The test cases for the robots movements
    """
    def test_move(self):
        """"
        Test a single movement
        """
        input_string = """
        PLACE 0,0,NORTH
        MOVE
        REPORT"""
        self.assertEqual(parse_text(input_string)[0], '0,1,NORTH')

    def test_rotation(self):
        """"
        Test a single rotation
        """
        input_string = """
        PLACE 0,0,NORTH
        LEFT
        REPORT"""
        self.assertEqual(parse_text(input_string)[0], '0,0,WEST')

    def test_full_movement(self):
        """"
        Test a few standard movements in conjunction
        """
        input_string = """
        PLACE 1,2,EAST
        MOVE
        MOVE
        LEFT
        MOVE
        REPORT"""
        self.assertEqual(parse_text(input_string)[0], '3,3,NORTH')

    def test_late_placement(self):
        """"
        Ensure only the latest placement gets used
        """
        input_string = """
        LEFT
        REPORT
        PLACE 0,0,NORTH
        MOVE
        REPORT
        """
        self.assertEqual(parse_text(input_string)[0], '0,1,NORTH')

    def test_invalid_placement(self):
        """"
        Verify bad locations are identified
        """
        input_string = """
        PLACE 0,5,NORTH
        PLACE -1,0,NORTH
        PLACE 0,0,SNORTH
        LEFT
        REPORT
        """
        self.assertEqual(parse_text(input_string)[0], 'Placement PLACE 0,5,NORTH in line 2 is not '
                                                      'valid PLACE, it needs to be in the format '
                                                      'PLACE X,Y,F')
        self.assertEqual(parse_text(input_string)[1], 'Placement PLACE -1,0,NORTH in line 3 is not '
                                                      'valid PLACE, it needs to be in the format '
                                                      'PLACE X,Y,F')
        self.assertEqual(parse_text(input_string)[2], 'Placement PLACE 0,0,SNORTH in line 4 is not '
                                                      'valid PLACE, it needs to be in the format '
                                                      'PLACE X,Y,F')

    def test_multiple_placements(self):
        """"
        Verify multiple placements are accepted
        """
        input_string = """
                PLACE 0,0,NORTH
                LEFT
                PLACE 0,0,NORTH
                MOVE
                REPORT
                """
        self.assertEqual(parse_text(input_string)[0], '0,1,NORTH')

    def test_multiple_reports(self):
        """"
        Verify multiple reports are recorded
        """
        input_string = """
                PLACE 0,0,NORTH
                LEFT
                REPORT
                PLACE 0,0,NORTH
                MOVE
                REPORT
                """
        self.assertEqual(parse_text(input_string)[0], '0,0,WEST')
        self.assertEqual(parse_text(input_string)[1], '0,1,NORTH')

    def test_invalid_parameters(self):
        """"
        Verify invalid inputs are identified and do not interfere with the execution
        """
        input_string = """
                PLACE 0,0,NORTH
                JUMP
                REPORT
                """
        self.assertEqual(parse_text(input_string)[0],
                         'command JUMP in line 3 is not valid, only use commands PLACE,MOVE,'
                         'RIGHT,LEFT,REPORT')

        self.assertEqual(parse_text(input_string)[1],
                         '0,0,NORTH')

    def test_no_report(self):
        """"
        Verify that the system does not return a result when no REPORT is given
        """
        input_string = """
                PLACE 0,0,NORTH
                LEFT
                """
        self.assertEqual(len(parse_text(input_string)), 0)
