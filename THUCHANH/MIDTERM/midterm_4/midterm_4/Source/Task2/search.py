import heapq
import math

class SearchAlgorithms:
    @staticmethod
    def a_star(graph, goal):
        start = graph.start
        path = [] 
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