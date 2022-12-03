from numpy import array
from Modules.Functions import cost_of_cells, find


class Table:
    def __init__(self, matrix):

        self.initial_matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

        # A 2D array which is g(n) of every cells
        self.board = cost_of_cells(matrix)

        # A 1D array of tuples which is location of each butters
        self.butter = find(matrix, 'b')

        # A 1D array of tuples which is location of each goals
        self.goals = find(matrix, 'p')

        # A tuple which is shows the location of robot
        self.robot = find(matrix, 'r')[0]


    def is_on_table(self, x, y):
        # print(f"w is: {self.width}, h is: {self.height}")
        return 0 <= x < self.width and 0 <= y < self.height

    def __str__(self):
        print("Given matrix is: ")
        return str(array(self.initial_matrix))
