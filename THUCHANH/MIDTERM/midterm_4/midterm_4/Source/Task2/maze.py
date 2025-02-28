import heapq
class MazeGraph:
    def __init__(self, maze):
        self.maze = maze
        self.start = None
        self.food_points = []
        self.rows = len(maze)
        self.cols = len(maze[0])

        # Find start position and collect food points and corners
        for i in range(self.rows):
            for j in range(self.cols):
                if maze[i][j] == 'P':
                    self.start = (i, j)
                elif maze[i][j] == '.':
                    self.food_points.append((i, j))
    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] != '%'

    def neighbors(self, pos):
        x, y = pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_neighbors = []
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if self.is_valid(neighbor):
                valid_neighbors.append(neighbor)
        return valid_neighbors

    def cost(self, pos1, pos2):
        return 1