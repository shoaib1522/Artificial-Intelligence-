from collections import deque

def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_moves(state):
    row, col = find_empty(state)
    moves = []
    if row > 0:
        moves.append('up')
    if row < 2:
        moves.append('down')
    if col > 0:
        moves.append('left')
    if col < 2:
        moves.append('right')
    return moves

def make_move(state, move):
    row, col = find_empty(state)
    new_state = [x[:] for x in state]
    if move == 'up':
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
    elif move == 'down':
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
    elif move == 'left':
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
    elif move == 'right':
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
    return new_state

def print_solution(path, state):
    print("Initial state:")
    for row in state:
        print(row)
    print("\nSteps:")
    for move in path:
        print("Move:", move)
        state = make_move(state, move)
        for row in state:
            print(row)
        print()

# DFS 
def dfs(start):
    stack = [(start, [])]
    visited = []
    
    while stack:
        state, path = stack.pop()
        visited.append(state)
        
        if is_goal(state):
            return path
        
        for move in get_moves(state):
            new_state = make_move(state, move)
            if new_state not in visited:
                stack.append((new_state, path + [move]))

    return None

# BFS 
def bfs(start):
    queue = deque([(start, [])])
    visited = []
    
    while queue:
        state, path = queue.popleft()
        visited.append(state)
        
        if is_goal(state):
            return path
        
        for move in get_moves(state):
            new_state = make_move(state, move)
            if new_state not in visited:
                queue.append((new_state, path + [move]))

    return None

# IDDFS 
def iddfs(start):
    depth = 0
    while True:
        result = dfs_limited(start, depth)
        if result is not None:
            return result
        depth += 1

def dfs_limited(state, limit):
    stack = [(state, [], 0)]
    
    while stack:
        current_state, path, depth = stack.pop()
        
        if depth > limit:
            continue
        
        if is_goal(current_state):
            return path
        
        for move in get_moves(current_state):
            new_state = make_move(current_state, move)
            stack.append((new_state, path + [move], depth + 1))
    
    return None

def main():
    puzzle = [[1, 2, 3],
              [4, 5, 6],
              [0, 7, 8]]

    print("DFS Solution:")
    dfs_solution = dfs(puzzle)
    if dfs_solution:
        print_solution(dfs_solution, puzzle)

    print("BFS Solution:")
    bfs_solution = bfs(puzzle)
    if bfs_solution:
        print_solution(bfs_solution, puzzle)

    print("IDDFS Solution:")
    iddfs_solution = iddfs(puzzle)
    if iddfs_solution:
        print_solution(iddfs_solution, puzzle)

if __name__ == "__main__":
    main()
