from maze import MazeGraph
from search import SearchAlgorithms

def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        maze = [line.strip() for line in file]
    return maze

def main():
    maze_file_path = input("Enter the path to the maze file: ")
    maze = read_maze_from_file(maze_file_path)

    maze_graph = MazeGraph(maze)
    food_points = maze_graph.food_points

    # Select search algorithm
    algorithm = input("Select the search algorithm (A* / UCS): ").strip().lower()

    # Validate the selected algorithm
    if algorithm not in ["a*", "ucs"]:
        print("Invalid algorithm selection.")
        return

    total_costs = []  # List to store total costs for each food point

    # Start recursion to find paths to food points
    find_paths(maze_graph, food_points, algorithm, total_costs)

    # Print the total sum of costs
    print("Total Sum of Costs:", sum(total_costs))


def find_paths(graph, food_points, algorithm, total_costs):
    if not food_points:
        return

    food_point = food_points[0]
    print("Food Point:", food_point)

    if algorithm == "a*":
        # Using A* algorithm
        path = SearchAlgorithms.a_star(graph, food_point)
    else:
        # Using UCS algorithm
        path = SearchAlgorithms.ucs(graph, graph.start, food_point)

    actions_list = get_actions_list(path)
    total_cost = len(path) - 1 if path else -1
    total_costs.append(total_cost)

    print(f"Search Algorithm: {algorithm.upper()}")
    print("Path:", path)
    print("Actions:", actions_list)
    print("Total Cost:", total_cost)
    print("-" * 50)

    # Remove the current food point and continue recursion
    graph.start = food_point
    food_points.remove(food_point)
    find_paths(graph, food_points, algorithm, total_costs)



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


# Pseudocode for main.py:
# function MAIN() 
#     maze_file_path ← USER INPUT
#     maze ← READ_MAZE_FROM_FILE(maze_file_path)
#     maze_graph ← MazeGraph(maze)
#     food_points ← maze_graph.food_points
#     algorithm ← USER INPUT
#     if algorithm not in ["a*", "ucs"] then PRINT "Invalid algorithm selection." and RETURN
#     total_costs ← EMPTY LIST
#     FIND_PATHS(maze_graph, food_points, algorithm, total_costs)
#     PRINT "Total Sum of Costs:", SUM(total_costs)

# function FIND_PATHS(graph, food_points, algorithm, total_costs)
#     if food_points is EMPTY then RETURN
#     food_point ← food_points[0]
#     PRINT "Food Point:", food_point
#     if algorithm == "a*" then path ← SearchAlgorithms.a_star(graph, food_point)
#     else path ← SearchAlgorithms.ucs(graph, graph.start, food_point)
#     actions_list ← GET_ACTIONS_LIST(path)
#     total_cost ← LENGTH(path) - 1 if path else -1
#     APPEND total_cost to total_costs
#     PRINT "Search Algorithm:", algorithm
#     PRINT "Path:", path
#     PRINT "Actions:", actions_list
#     PRINT "Total Cost:", total_cost
#     PRINT "-" * 50
#     graph.start ← food_point
#     REMOVE food_point from food_points
#     FIND_PATHS(graph, food_points, algorithm, total_costs)

# function GET_ACTIONS_LIST(path)
#     actions_list ← EMPTY LIST
#     for i in range(LENGTH(path) - 1) do
#         curr_pos ← path[i]
#         next_pos ← path[i + 1]
#         if next_pos[0] < curr_pos[0] then APPEND "North" to actions_list
#         else if next_pos[0] > curr_pos[0] then APPEND "South" to actions_list
#         else if next_pos[1] < curr_pos[1] then APPEND "West" to actions_list
#         else if next_pos[1] > curr_pos[1] then APPEND "East" to actions_list
#     RETURN actions_list

# if __name__ == "__main__" then CALL MAIN()
