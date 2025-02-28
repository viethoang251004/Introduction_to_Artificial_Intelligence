from copy import deepcopy
from graphviz import Digraph

dot = Digraph()
dot.node('0', '182\n_43\n765')
dot.node('1', '182\n4_3\n765')
dot.node('2', '_82\n143\n765')
dot.node('3', '182\n743\n_65')
dot.edge('0', '1', 'L')
dot.edge('0', '2', 'D')
dot.edge('0', '3', 'U')

dot


class Node:

    def __init__(self, state, action=None, parent=None):
        self.state = state  # 2D list (3x3)
        self.id = str(self)  # identifier of node
        self.action = action
        self.parent = parent

    def __str__(self):
        '''
        # TODO 1
        Return a string representing the state of the node.
        Note to remember the 0 digit by '_'
        e.g., '182\n_43\n765'
        '''
        return '\n'.join(''.join('_' if item == 0 else str(item) for item in row) for row in self.state)

    def get_successors(self):
        '''
        # TODO 2
        Return the list of successors of the state (self).
        '''
        directions = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]
        # empty_pos = [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == '_'][0]
        empty_pos_list = [(i, j) for i in range(3)
                          for j in range(3) if self.state[i][j] == '_']
        if empty_pos_list:
            empty_pos = empty_pos_list[0]
        else:
            raise ValueError(
                "Không tìm thấy vị trí trống ('_') trong trạng thái")

        successors = []

        for action, dx, dy in directions:
            new_x, new_y = empty_pos[0] + dx, empty_pos[1] + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = deepcopy(self.state)
                new_state[empty_pos[0]][empty_pos[1]
                                        ], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_pos[0]][empty_pos[1]]
                successors.append(Node(new_state, action, self))

        return successors

    def get_successor(self, action, state):
        pi, pj = self.get_blank_pos(state)
        pi, pj = self.get_dest_pos(action, pi, pj)
        if 0 <= pi and pi < 3 and 0 <= pj and pj < 3:
            if action == 'L':
                state[pi][pj - 1] = state[pi][pj]
            if action == 'R':
                state[pi][pj + 1] = state[pi][pj]
            if action == 'U':
                state[pi-1][pj] = state[pi][pj]
            if action == 'D':
                state[pi+1][pj] = state[pi][pj]
            state[pi][pj] = 0
            return state
        return None

    def get_dest_pos(self, action, pi, pj):
        if action == 'L':
            pj += 1
        if action == 'R':
            pj -= 1
        if action == 'U':
            pi += 1
        if action == 'D':
            pi -= 1
        return pi, pj

    def get_blank_pos(self, state):
        '''
        # TODO 3
        Return the location (i, j) of the 0 digit (blank cell).
        '''
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return i, j

    def get_id(self):
        return self.id

    def get_node_str(self):
        return str(self)

    def get_action(self):
        return self.action

    def draw(self, dot):
        dot.node(self.get_id(), self.get_node_str())
        if self.parent is not None:
            dot.edge(self.parent.get_id(), self.get_id(), self.get_action())


def expand(dot, n):
    successors = n.get_successors()
    for s in successors:
        s.draw(dot)


n = Node([[1, 8, 2],
          [0, 4, 3],
          [7, 6, 5]])
dot = Digraph()
n.draw(dot)
expand(dot, n)

dot
