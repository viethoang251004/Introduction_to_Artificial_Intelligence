import heapq
import math

class SearchAlgorithms:
    @staticmethod
    def a_star(graph, goal):
        start = graph.start
        path = [] # path from src to dst

        # Initialize priority queue
        open_set = [(0, start)]
        came_from = {}
        g_score = {start: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = SearchAlgorithms.reconstruct_path(came_from, current)
                break

            for neighbor in graph.neighbors(current):
                tentative_g_score = g_score[current] + graph.cost(current, neighbor)
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + SearchAlgorithms.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return path

    @staticmethod
    def reconstruct_path(came_from, current):
        path = []
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        return list(reversed(path))

    @staticmethod
    def heuristic(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
        
    @staticmethod
    def ucs(graph, start, goal):
        # Uniform Cost Search implementation
        open_set = [(0, start)]
        came_from = {}
        cost_so_far = {start: 0}

        while open_set:
            cost, current = heapq.heappop(open_set)

            if current == goal:
                break

            for neighbor in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, neighbor)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(open_set, (new_cost, neighbor))
                    came_from[neighbor] = current

        path = []
        while current is not None:
            path.append(current)
            current = came_from.get(current)

        return list(reversed(path))


# Pseudocode for search.py:
# class SearchAlgorithms:
#     function A_STAR(graph, goal):
#         start ← graph.start
#         path ← EMPTY LIST
#         open_set ← [(0, start)]
#         came_from ← EMPTY DICTIONARY
#         g_score ← {start: 0}
#         while open_set is not EMPTY:
#             _, current ← REMOVE MINIMUM ELEMENT from open_set
#             if current == goal then
#                 path ← RECONSTRUCT_PATH(came_from, current)
#                 break
#             for each neighbor in graph.neighbors(current):
#                 tentative_g_score ← g_score[current] + graph.cost(current, neighbor)
#                 if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                     came_from[neighbor] ← current
#                     g_score[neighbor] ← tentative_g_score
#                     f_score ← tentative_g_score + HEURISTIC(neighbor, goal)
#                     ADD (f_score, neighbor) to open_set
#         return path

#     function RECONSTRUCT_PATH(came_from, current):
#         path ← EMPTY LIST
#         while current is not None:
#             ADD current to path
#             current ← came_from.get(current)
#         return REVERSE(path)

#     function HEURISTIC(pos, goal):
#         return ABS(pos[0] - goal[0]) + ABS(pos[1] - goal[1])

#     function UCS(graph, start, goal):
#         open_set ← [(0, start)]
#         came_from ← EMPTY DICTIONARY
#         cost_so_far ← {start: 0}
#         while open_set is not EMPTY:
#             cost, current ← REMOVE MINIMUM ELEMENT from open_set
#             if current == goal then
#                 break
#             for each neighbor in graph.neighbors(current):
#                 new_cost ← cost_so_far[current] + graph.cost(current, neighbor)
#                 if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
#                     cost_so_far[neighbor] ← new_cost
#                     ADD (new_cost, neighbor) to open_set
#                     came_from[neighbor] ← current
#         path ← EMPTY LIST
#         while current is not None:
#             ADD current to path
#             current ← came_from.get(current)
#         return REVERSE(path)
