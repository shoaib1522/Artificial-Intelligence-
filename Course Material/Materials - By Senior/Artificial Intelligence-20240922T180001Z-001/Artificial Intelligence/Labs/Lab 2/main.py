class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def path(self):
        path = []
        node = self
        while node:
            if node.action:
                path.append(node.action)
            node = node.parent
        return list(reversed(path))


class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.size = int(len(initial_state) ** 0.5)

    def actions(self, state):
        actions = []
        empty_index = state.index(0)
        row, col = divmod(empty_index, self.size)

        if col > 0:
            actions.append('left')
        if col < self.size - 1:
            actions.append('right')
        if row > 0:
            actions.append('up')
        if row < self.size - 1:
            actions.append('down')

        return actions

    def result(self, state, action):
        empty_index = state.index(0)
        row, col = divmod(empty_index, self.size)
        new_state = state[:]
        if action == 'left':
            new_col = col - 1
            new_index = row * self.size + new_col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
        elif action == 'right':
            new_col = col + 1
            new_index = row * self.size + new_col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
        elif action == 'up':
            new_row = row - 1
            new_index = new_row * self.size + col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
        elif action == 'down':
            new_row = row + 1
            new_index = new_row * self.size + col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
        return new_state

    def is_goal(self, state):
        return state == self.goal_state

    def is_solvable(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversions += 1
        row, _ = divmod(state.index(0), self.size)
        if self.size % 2 == 0:
            return (inversions + row) % 2 == 0
        return inversions % 2 == 0


def depth_first_iterative_deepening(problem):
    depth_limit = 0
    while True:
        result = depth_limited_search(problem, depth_limit)
        if result is not None:
            return result
        depth_limit += 1


def depth_limited_search(problem, depth_limit):
    visited = set()
    initial_node = Node(problem.initial_state)
    return recursive_depth_limited_search(problem, initial_node, depth_limit, visited)


def recursive_depth_limited_search(problem, node, depth_limit, visited):
    if problem.is_goal(node.state):
        return node.path()

    if node.depth == depth_limit:
        return None

    visited.add(tuple(node.state))

    for action in problem.actions(node.state):
        child_state = problem.result(node.state, action)
        if tuple(child_state) not in visited:
            child_node = Node(child_state, node, action)
            result = recursive_depth_limited_search(problem, child_node, depth_limit, visited)
            if result is not None:
                return result

    return None


def main():
    puzzle = EightPuzzle([1, 5, 3, 2, 7, 4, 6, 0, 8])

    if puzzle.is_solvable(puzzle.initial_state):
        solution = depth_first_iterative_deepening(puzzle)
        if solution is None:
            print("No solution found.")
        else:
            print("Solution found:")
            print(solution)
    else:
        print("The puzzle is not solvable.")

main()
