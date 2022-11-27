from Classes.Table import Table
from Classes.Node import Node


def is_it_validate_action(x, y, robot_x, robot_y, table_board):
    flag = True

    # After action robot must be on table.
    if not table_board.is_on_table(robot_x + x, robot_y + y):
        flag = False

    # Diagonal action is not allowed.
    if x * y == 1 or x * y == -1:
        flag = False

    # Robot can not go to a block cells.
    if table_board.board[robot_y][robot_x] == float('inf'):
        flag = False

    return flag


# We are going to check an action like (1, 0) validate or not
# and if it was, we'll push butters and save that in new_nodes[].
def check_action(x, y, node, table_board: Table):
    robot_x = node.robot[1]
    robot_y = node.robot[0]
    successor_array = []

    result = is_it_validate_action(x, y, robot_x, robot_y, table_board)
    if result:
        if not (robot_y + y, robot_x + x) in node.butter:
            """ It means there is no butters in the cell which robot is going to. """
            successor_array.append(
                (
                    Node((robot_y + y, robot_x + x), node.butter),
                    (y, x),
                    max(table_board[robot_y + y][robot_x + x],
                        table_board[robot_y][robot_x])
                 )
            )
        else:
            """ It means in spit of the last if statement there is a butter in that cell. """
            height, width = table_board.height, table_board.width
            # After moving robot to that cell the butter will pushed by robot
            #   therefore, it must be checked the butter won't drop from table
            if (y == -1 and robot_y == 1) or (y == 1 and robot_y == height-2) \
                    or (x == -1 and robot_x == 1) or (x == 1 and robot_x == width - 2):
                return

            else:   # Movement of robot doesn't cause butter to drop from table.
                # If there was a block cell or another butter in front of the butter:
                if table_board.board[robot_y + 2*y][robot_x + 2*x] == float('inf') \
                        or table_board.board[robot_y + 2*y][robot_x + 2*x] in table_board.butter:
                    return

                # After movement of robot butter on point:
                if (robot_y + y, robot_x + x) in table_board.goals:
                    return

                # Now the action is validated and the butter won't fall off the table
                #   and there is no problem with pushing butter by robot!
                #   so, it's time to make a movement.

                # for making a movement we must update the list of butters and robot positions.
                butters_after_movement = node.butter.copy()
                butters_after_movement.remove((robot_y + y, robot_x + x))
                butters_after_movement.append((robot_y + 2*y, robot_x + 2*x))
                successor_array.append(
                    (
                        Node((robot_y + y, robot_x + x), butters_after_movement),
                        (y, x),
                        max(table_board.board[robot_y + y][robot_x + x],
                            table_board.board[robot_y][robot_x])
                    )
                )
    return successor_array
