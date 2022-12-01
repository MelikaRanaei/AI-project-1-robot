from Classes.Table import Table
from Modules.Action import check_action


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

