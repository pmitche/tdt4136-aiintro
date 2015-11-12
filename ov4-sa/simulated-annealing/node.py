__author__ = 'paulpm / Paul Philip Mitchell'
from copy import deepcopy
import random


class Node(object):
    UP = 0
    DOWN = 2

    def __init__(self, board, eggs=None):
        self.board = board
        # If parameter eggs is passed to constructor, set as eggs - otherwise, create boolean list
        self.eggs = eggs or [[False for row in range(board["columns"])] for col in range(board["rows"])]

    """
    Generates neighbors of node by moving an egg either up or down.
    Loops through the board and generates neighboring Nodes
    """
    def create_neighbors(self):
        neighbors = []
        for x in range(self.board["columns"]):
            for y in range(self.board["rows"]):
                if self.eggs[y][x]:
                    if self.is_legal_move(x, y, self.UP):
                        neighbors.append(Node(self.board, self.clone_eggs(self.eggs, x, y, self.UP)))
                    if self.is_legal_move(x, y, self.DOWN):
                        neighbors.append(Node(self.board, self.clone_eggs(self.eggs, x, y, self.DOWN)))
        return neighbors

    """
    Deepcopies an eggs-list and changes original list based on changes in directions.
    """
    def clone_eggs(self, eggs, x, y, direction):
        target = deepcopy(eggs)
        target[y][x] = False
        if direction == self.UP:
            target[y-1][x] = True
        if direction == self.DOWN:
            target[y+1][x] = True
        return target

    """
    This is the objective function. Calculates the score of a given node, based on if constraints are met or not.
    Returns a value between 0 and 1.
    """
    def evaluate(self):
        rows = self.board["rows"]
        cols = self.board["columns"]
        k = self.board["k"]

        row_k = [0 for i in range(cols)]
        col_k = [0 for i in range(rows)]
        left_diagonal = [0 for i in range(rows + cols - 1)]
        right_diagonal = [0 for i in range(rows + cols - 1)]
        evaluation = 0

        # Counts eggs in every direction.
        for y in range(rows):
            for x in range(cols):
                if self.eggs[y][x]:
                    row_k[y] += 1
                    col_k[x] += 1
                    right_diagonal[cols - x + y - 1] += 1
                    left_diagonal[x + y] += 1

        # Increments evaluation
        for y in range(rows):
            for x in range(cols):
                if self.eggs[y][x]:
                    if row_k[y] <= k and col_k[x] <= k and right_diagonal[cols - x + y - 1] <= k and left_diagonal[x + y] <= k:
                        evaluation += 1

        return evaluation / float(rows * k)

    """
    Generates a starting board. K eggs are placed on the board in random order.
    """
    def set_start_node(self):
        for i in range(self.board["columns"]):
            counter = 0
            while counter < self.board["k"]:
                row = random.randint(0, self.board["rows"]-1)
                if not self.eggs[row][i]:
                    self.eggs[row][i] = True
                    counter += 1

    """
    Board logic to account for eggs mistakenly being placed either on top of each other or outside the axises.
    """
    def is_legal_move(self, x, y, direction):
        if direction == self.UP and y - 1 >= 0 and not self.eggs[y-1][x]:
            return True
        elif direction == self.DOWN and y + 1 < self.board["rows"] and not self.eggs[y+1][x]:
            return True
        return False

    """
    Representation of a Node.
    """
    def __str__(self):
        result = ""
        for y in range(self.board["rows"]):
            for x in range(self.board["columns"]):
                if self.eggs[y][x]:
                    result += " O "
                else:
                    result += " - "
            result += "\n"
        return result





