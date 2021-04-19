import unittest

class Matrix():
    def __init__(self, maze):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

    def set_neighbor_coords(self, coordinate):
        neighbors = set()
        x = coordinate[0]
        y = coordinate[1]
        distance = 0 if self.maze[x][y] == -2 else self.maze[x][y]

        if x+1 < self.height:
            if self.maze[x+1][y] == 0:
                self.maze[x+1][y] = distance+1
                neighbors.add((x+1, y))
        if x-1 >= 0:
            if self.maze[x-1][y] == 0:
                self.maze[x-1][y] = distance+1
                neighbors.add((x-1,y))
        if y+1 < self.width:
            if self.maze[x][y+1] == 0:
                self.maze[x][y+1] = distance+1
                neighbors.add((x, y+1))
        if y-1 >= 0:
            if self.maze[x][y-1] == 0:
                self.maze[x][y-1] = distance+1
                neighbors.add((x,y-1))

        return neighbors

    def find_distances(self):
        explore = []

        for row in range(self.height):
            for column in range(self.width):
                if self.maze[row][column] == -2:
                    explore.append((row, column))

        while(len(explore) > 0):
            coordinate = explore[0]
            explore.remove(coordinate)
            result = self.set_neighbor_coords(coordinate)
            if result is not None:
                explore.extend(result)

        return self.maze

class TestMatrix(unittest.TestCase):
    def test_Matrix1(self):

        matrix = Matrix([[0,0,-1,-2],[0,0,0,0]])

        output = matrix.find_distances()
        self.assertEqual(output, [[5,4,-1,-2],[4,3,2,1]])

    def test_Matrix2(self):

        matrix = Matrix([[0,0,-1,-2,0],[0,0,-1,0,0],[0,0,-1,0,0]])

        output = matrix.find_distances()
        self.assertEqual(output, [[0, 0, -1, -2, 1], [0, 0, -1, 1, 2], [0, 0, -1, 2, 3]])

unittest.main(exit=False)
