"""The module responsible for parsing the commands and calling the appropriate functions of how
the robot moves """
from simulator.direction import get_position, get_valid_direction
from simulator.valid_position import is_valid_position
from simulator.toy_robot import ToyRobot


def parse_text(robot_instructions: str):
    """
    The function that executes the Toy Robot simulation based on the string sent in
    :param robot_instructions: A string that has all the instructions for how the robot should move
    :return: A list of strings for each of the reported positions and invalid commands
    """
    check_valid_first_placement = False
    confirmed_placement = False
    robot = None

    output_history = []
    commands = robot_instructions.splitlines()
    for i in range(len(commands)):
        command = commands[i].strip()
        if not confirmed_placement and command[:5] == "PLACE":
            check_valid_first_placement = True
        if check_valid_first_placement or confirmed_placement:
            if command == "MOVE":
                robot.move()
            elif command == "LEFT":
                robot.rotate_left()
            elif command == "RIGHT":
                robot.rotate_right()
            elif command == "REPORT":
                output_history.append(robot.get_location())
            elif command[:5] == "PLACE":
                location_section = command.split(" ")
                location_elements = location_section[1].split(",")
                x_coordinate = int(location_elements[0])
                y_coordinate = int(location_elements[1])
                direction = location_elements[2]
                if is_valid_position(x_coordinate, y_coordinate) and get_valid_direction(direction):
                    robot = ToyRobot(x_coordinate, y_coordinate, get_position(direction))
                    confirmed_placement = True
                else:
                    check_valid_first_placement = False
                    output_history.append(
                        f"Placement {command} in line {(i + 1)} is not valid PLACE, it needs to be "
                        f"in the format PLACE X,Y,F")
            elif len(command) > 0:
                output_history.append(
                    f"command {command} in line {(i + 1)} is not valid, only use commands PLACE,"
                    f"MOVE,RIGHT,LEFT,REPORT")
    return output_history
