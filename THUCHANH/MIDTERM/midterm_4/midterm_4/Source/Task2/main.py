from maze import MazeGraph
from search import SearchAlgorithms
import sys

def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        maze = [line.strip() for line in file]
    return maze

def find_paths(graph, food_points, algorithm, total_costs, output_file):
    if not food_points:
        return

    food_point = food_points[0]
    output_file.write(f"Food Point: {food_point}\n")

    if algorithm == "a*":
        path = SearchAlgorithms.a_star(graph, food_point)
    else:
        path = SearchAlgorithms.ucs(graph, graph.start, food_point)

    actions_list = get_actions_list(path)
    total_cost = len(path) - 1 if path else -1
    total_costs.append(total_cost)

    output_file.write(f"Search Algorithm: {algorithm.upper()}\n")
    output_file.write(f"Path: {path}\n")
    output_file.write(f"Actions: {actions_list}\n")
    output_file.write(f"Total Cost: {total_cost}\n")
    output_file.write("-" * 50 + "\n")

    # Remove the current food point and continue recursion
    graph.start = food_point
    food_points.remove(food_point)
    find_paths(graph, food_points, algorithm, total_costs, output_file)

def main():
    maze_file_path = input("Enter the path to the maze file: ")
    maze = read_maze_from_file(maze_file_path)

    maze_graph = MazeGraph(maze)
    food_points = maze_graph.food_points

    algorithm = input("Select the search algorithm (A* / UCS): ").strip().lower()

    # Validate the selected algorithm
    if algorithm not in ["a*", "ucs"]:
        print("Invalid algorithm selection.")
        return

    total_costs = []  # List to store total costs for each food point

    # Redirect output to a file
    with open("out.txt", "w") as output_file:
        # Start recursion to find paths to food points
        find_paths(maze_graph, food_points, algorithm, total_costs, output_file)

        print("Total Sum of Costs:", sum(total_costs))
        output_file.write(f"Total Sum of Costs: {sum(total_costs)}\n")


def get_actions_list(path):
    actions_list = []
    if path:
        for i in range(len(path) - 1):
            curr_pos = path[i]
            next_pos = path[i + 1]
            if next_pos[0] < curr_pos[0]:
                actions_list.append("North")
            elif next_pos[0] > curr_pos[0]:
                actions_list.append("South")
            elif next_pos[1] < curr_pos[1]:
                actions_list.append("West")
            elif next_pos[1] > curr_pos[1]:
                actions_list.append("East")
    return actions_list


if __name__ == "__main__":
    main()
