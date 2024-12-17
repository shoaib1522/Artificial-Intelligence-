import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def generate_children(self):
        children = []
        empty_index = self.state.index(0)
        
        row = empty_index // 3
        col = empty_index % 3
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            
            if new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3:
                new_index = new_row * 3 + new_col
                
                new_state = self.state[:]
                
                new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                
                h_cost = self.calculate_heuristic(goal_state)
                
                child_node = PuzzleNode(new_state, self, move, self.g_cost + 1, h_cost)
                
                children.append(child_node)
        
        return children
    def calculate_heuristic(self, goal_state):
        distance = 0
        for i in range(1, 9):
            current_pos = self.state.index(i)
            goal_pos = goal_state.index(i)
            
            current_row = current_pos // 3
            current_col = current_pos % 3
            
            goal_row = goal_pos // 3
            goal_col = goal_pos % 3
        
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        
        return distance

class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        if not self.is_solvable(self.start_state):
            return None

        open_list = []
        closed_list = set()
        
        start_node = PuzzleNode(self.start_state, None, None, 0, self.calculate_heuristic(self.start_state))
        
        heapq.heappush(open_list, start_node)
        
        while open_list:
            current_node = heapq.heappop(open_list)
            
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)
            
            closed_list.add(tuple(current_node.state))
            
            children = current_node.generate_children()
            
            for child in children:
                if tuple(child.state) not in closed_list:
                    heapq.heappush(open_list, child)
        
        return None

    def trace_solution(self, node):
        path = []
        
        while node is not None:
            path.append(node)
            node = node.parent
        
        return path[::-1]

    def is_solvable(self, state):
        inversions = 0
        
        for i in range(8):
            for j in range(i + 1, 9):
                if state[i] and state[j] and state[i] > state[j]:
                    inversions += 1
        
        return inversions % 2 == 0

    def calculate_heuristic(self, state):
        distance = 0
        for i in range(1, 9):
            current_pos = state.index(i)
            goal_pos = self.goal_state.index(i)
            
            current_row = current_pos // 3
            current_col = current_pos % 3
            
            goal_row = goal_pos // 3
            goal_col = goal_pos % 3
            
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        
        return distance

def print_puzzle(state):
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            if tile == 0:
                print(" ", end=" ")
            else:
                print(tile, end=" ")
        print()
    print()

initial_state = [1, 2, 3, 4,  0,5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solver = AStarSolver(initial_state, goal_state)
solution_path = solver.solve()

if solution_path:
    print("Solution steps:")
    for step in solution_path:
        print_puzzle(step.state)
else:
    print("No solution found.")
