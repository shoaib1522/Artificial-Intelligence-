import heapq

class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.h_cost = h_cost

    def find_zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_children(self):
        children = []
        i, j = self.find_zero_position()
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for d in directions:
            if 0 <= d[0] < 3 and 0 <= d[1] < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[d[0]][d[1]] = new_state[d[0]][d[1]], new_state[i][j]
                children.append(Node(new_state, self, (i, j), 0))
        return children

    def calculate_heuristic(self, goal_state):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    for x in range(3):
                        for y in range(3):
                            if goal_state[x][y] == self.state[i][j]:
                                h += abs(i - x) + abs(j - y)
        return h

    def __lt__(self, other):
        return self.h_cost < other.h_cost

class GreedyBestFirstSearch:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        open_list = []
        start_node = Node(self.start_state, None, None, 0)
        heapq.heappush(open_list, (start_node.h_cost, start_node))
        visited = []
        
        while open_list:
            _, current_node = heapq.heappop(open_list)
            
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)
            
            visited.append(current_node.state)

            for child in current_node.generate_children():
                if child.state not in visited:
                    child.h_cost = child.calculate_heuristic(self.goal_state)
                    heapq.heappush(open_list, (child.h_cost, child))

    def trace_solution(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]

    def print_solution(self, solution):
        for step, node in enumerate(solution):
            print(f"Step {step}:")
            for row in node.state:
                print(row)
            print()

start_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

gbfs = GreedyBestFirstSearch(start_state, goal_state)
solution = gbfs.solve()

print("Solution:")
gbfs.print_solution(solution)