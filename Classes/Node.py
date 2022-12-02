from Classes.Table import Table
from Classes.Color import Colors
# from Modules.Action import check_action


def is_it_validate_action(x, y, robot_x, robot_y, table_board):
    flag = True
    print(f"robot is : {robot_x, robot_y} and with move: {(x, y)} wants to go: {robot_x+x, robot_y+y}")
    if not table_board.is_on_table(robot_x + x, robot_y + y):
        print(Colors.WARNING + f"movement " + Colors.UNDERLINE + f"{(x, y)}" + Colors.reset
              + Colors.WARNING + " is not allowed because not on table.\n" + Colors.reset)
        flag = False

    # Diagonal action is not allowed.
    if x * y == 1 or x * y == -1:
        print(Colors.WARNING + f"movement " + Colors.UNDERLINE + f"{(x, y)}" + Colors.reset
              + Colors.WARNING + " is not allowed because it is diagonal.\n" + Colors.reset)
        flag = False

    # Robot can not go to a block cells.
    xx = robot_x + x
    yy = robot_y + y
    height = table_board.height
    if table_board.board[height-yy-1][xx] == float('inf'):
        print(Colors.WARNING + f"movement " + Colors.UNDERLINE + f"{(x, y)}" + Colors.reset
              + Colors.WARNING + " is not allowed because it is 'X' cell.\n" + Colors.reset)
        flag = False

    return flag


# We are going to check an action like (1, 0) validate or not
# and if it was, we'll push butters and save that in new_nodes[].
def check_action(x, y, node, table_board: Table):
    robot_y = node.robot[1]
    robot_x = node.robot[0]
    height, width = table_board.height, table_board.width
    successor_array = []

    result = is_it_validate_action(x, y, robot_x, robot_y, table_board)
    # print(result)
    if result:
        if not (robot_y + y, robot_x + x) in node.butter:
            """ It means there is no butters in the cell which robot is going to. """
            print(f"width: {table_board.width}, height: {height}")

            print(f"table_board[Rx][Ry]: {table_board.board[height - robot_y - 1][robot_x]}")
            # print(f"table_board[Rx][Ry]: {table_board.board[robot_x][robot_y]}")
            xx = robot_x+x
            yy = robot_y+y
            print(f"table_board[Rx+x][Ry+y]: {table_board.board[height-yy-1][xx]}\n")
            successor_array.append(
                (
                    Node((robot_y + y, robot_x + x), node.butter),
                    (x, y),
                    max(table_board.board[height-yy-1][xx],
                        table_board.board[height - robot_y - 1][robot_x])
                 )
            )
        else:
            """ It means in spit of the last if statement there is a butter in that cell. """
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

                print(f"width: {table_board.width}, height: {height}")
                print(f"table_board[Rx][Ry]: {table_board.board[height-robot_y-1][robot_x]}")
                xx = robot_x + x
                yy = robot_y + y
                print(f"table_board[Rx+x][Ry+y]: {table_board.board[height - yy - 1][xx]}\n")
                # print(f"table_board[Rx+x][Ry+y]: {table_board.board[robot_x+x][robot_y+y]}\n")
                successor_array.append(
                    (
                        Node((robot_y + y, robot_x + x), butters_after_movement),
                        (x, y),
                        max(table_board.board[height - yy - 1][xx],
                            table_board.board[height - robot_y - 1][robot_x])
                    )
                )
    return successor_array


class Node:

    def __init__(self, robot, butter=[]):
        self.robot = robot
        self.butter = butter

    def __hash__(self):
        hash_of_current_node = 0
        for i in self.butter:
            hash_of_current_node += hash(self.butter[i])
        return hash_of_current_node + hash(self.robot)

    @staticmethod
    def successor(current_node: 'Node', table_board: Table):
        """ We want to figure out what is the subsequent nodes of the current node
            by moving around in the table from this node """

        subsequent_node = []

        subsequent_node.extend(check_action(1, 0, current_node, table_board))
        subsequent_node.extend(check_action(0, 1, current_node, table_board))
        subsequent_node.extend(check_action(-1, 0, current_node, table_board))
        subsequent_node.extend(check_action(0, -1, current_node, table_board))

        return subsequent_node

    @staticmethod
    def is_goal_node(node: 'Node', goals):
        for butter in node.butter:
            if butter in goals:
                return True
        return False
