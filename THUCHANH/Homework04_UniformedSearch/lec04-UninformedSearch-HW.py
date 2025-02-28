import os
import heapq

# Directed, weighted graphs


class Graph:
    def __init__(self):
        self.AL = dict()  # adjacency list
        self.V = 0
        self.E = 0

    def __str__(self):
        res = 'V: %d, E: %d\n' % (self.V, self.E)
        for u, neighbors in self.AL.items():
            line = '%d: %s\n' % (u, str(neighbors))
            res += line
        return res

    def __init__(self, V):
        self.V = V
        self.AL = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.AL[u].append(v)
        self.AL[v].append(u)

    def print(self):
        print(str(self))

    def load_from_file(self, filename):
        # '''
        #     Example input file:
        #         V E
        #         u v w
        #         u v w
        #         u v w
        #         ...

        #     # input.txt
        #     7 8
        #     0 1 5
        #     0 2 6
        #     1 3 12
        #     1 4 9
        #     2 5 5
        #     3 5 8
        #     3 6 7
        #     4 6 4
        # '''
        if os.path.exists(filename):
            with open(filename) as g:
                self.V, self.E = [int(it) for it in g.readline().split()]
                for line in g:
                    u, v, w = [int(it) for it in line.strip().split()]
                    if u not in self.AL:
                        self.AL[u] = []
                    self.AL[u].append((v, w))


g = Graph()
g.load_from_file('input.txt')
g.print()
# Khởi tạo đồ thị với 6 đỉnh
g = Graph(6)

# Thêm cạnh giữa các đỉnh
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

# Thêm đỉnh 5 với các đỉnh kề [3, 4]
g.AL.append([3, 4])

class SearchStrategy:
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst
        return expanded, path

class BFS(SearchStrategy):
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst

        visited = [False] * g.V
        queue = [(src, [src])]  # Queue stores vertex and its path

        while queue:
            vertex, current_path = queue.pop(0)
            expanded.append(vertex)

            if vertex == dst:
                path = current_path
                break

            visited[vertex] = True

            for neighbour, _ in g.AL[vertex]:
                if not visited[neighbour]:
                    queue.append((neighbour, current_path + [neighbour]))
                    visited[neighbour] = True

        return expanded, path


class DFS(SearchStrategy):
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst

        visited = [False] * g.V

        def dfs_util(vertex, current_path):
            nonlocal path

            expanded.append(vertex)
            visited[vertex] = True

            if vertex == dst:
                path = current_path
                return True

            for neighbour, _ in g.AL[vertex]:
                if not visited[neighbour]:
                    if dfs_util(neighbour, current_path + [neighbour]):
                        return True

            return False

        dfs_util(src, [src])

        return expanded, path

class UCS(SearchStrategy):
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst

        visited = [False] * g.V
        queue = [(0, src, [src])]  # Priority queue stores (cost, vertex, path)

        while queue:
            cost, vertex, current_path = heapq.heappop(queue)
            expanded.append(vertex)

            if vertex == dst:
                path = current_path
                break

            if visited[vertex]:
                continue

            visited[vertex] = True

            for neighbour, edge_cost in g.AL[vertex]:
                if not visited[neighbour]:
                    heapq.heappush(queue, (cost + edge_cost, neighbour, current_path + [neighbour]))

        return expanded, path

class DLS(SearchStrategy):
    def __init__(self, LIM):
        self.LIM = LIM

    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst

        visited = [False] * g.V

        def dls_util(vertex, current_path, depth):
            nonlocal path

            expanded.append(vertex)
            visited[vertex] = True

            if vertex == dst:
                path = current_path
                return True

            if depth >= self.LIM:
                return False

            for neighbour, _ in g.AL[vertex]:
                if not visited[neighbour]:
                    if dls_util(neighbour, current_path + [neighbour], depth + 1):
                        return True

            return False

        dls_util(src, [src], 0)

        return expanded, path

class IDS(SearchStrategy):
    def __init__(self, MAX_LIM):
        self.MAX_LIM = MAX_LIM

    def search(self, g: Graph, src: int, dst: int) -> tuple:
        expanded = []  # list of expanded vertices in the traversal order
        path = []  # path from src to dst

        for depth_limit in range(self.MAX_LIM + 1):  # depth_limit can be up to MAX_LIM
            dls = DLS(depth_limit)
            expanded, path = dls.search(g, src, dst)

            if path:
                break

        return expanded, path


bfs = BFS()
dfs = DFS()
ucs = UCS()
dls = DLS(LIM=3)
ids = IDS(MAX_LIM=5)

for stg in [bfs, dfs, ucs, dls, ids]:
    print(stg)
    expanded, path = stg.search(g, 0, g.V-1)
    print(expanded)
    print(path)
