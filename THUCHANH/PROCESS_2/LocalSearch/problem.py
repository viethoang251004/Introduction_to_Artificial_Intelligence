import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

class Problem:
    def __init__(self, filename):
        self.filename = filename
        self.load_state_space(filename)

    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        self.X = np.arange(w)
        self.Y = np.arange(h)
        self.Z = img
        self.X, self.Y = np.meshgrid(self.X, self.Y)  # Tạo ma trận tọa độ X và Y từ X và Y ban đầu

    def show(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        plt.show()

    def draw_path(self, path):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        path_x = [state[0] for state in path]
        path_y = [state[1] for state in path]
        path_z = [self.Z[state[1], state[0]] for state in path]
        ax.plot(path_x, path_y, path_z, 'r-', zorder=3, linewidth=0.5)
        ax.set_title('Path Visualization on State Space Surface')
        ax.set_xlabel('X coordinate')
        ax.set_ylabel('Y coordinate')
        ax.set_zlabel('Z value (Pixel Intensity)')
        plt.show()

    def evaluate_state(self, state):
        x,y = state
        return self.Z[y, x]


    def get_random_state(self):
        x = random.randint(0, self.Z.shape[1] - 1)
        y = random.randint(0, self.Z.shape[0] - 1)
        return (x, y)

    def get_highest_valued_successor(self, state):
        neighbors = self.get_neighbors(state)  # Lấy danh sách các người hàng xóm
        best_neighbor = None
        best_evaluation = float('-inf')
        for neighbor in neighbors:
            evaluation = self.evaluate_state(neighbor)
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_neighbor = neighbor
        return best_neighbor

    def get_neighbors(self, state):
        # Generate and return the neighbors of the given state
        x, y = state
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-way connectivity
        neighbors = [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < self.Z.shape[1] and 0 <= y + dy < self.Z.shape[0]]
        return neighbors

    def is_edge_state(self, state):
        x, y = state
        if x == 0 or y == 0 or x == len(self.X) - 1 or y == len(self.Y) - 1:
            return True
        else:
            return False
    
    def get_initial_state(self):
        # Trả về một trạng thái ban đầu ngẫu nhiên
        return self.get_random_state()