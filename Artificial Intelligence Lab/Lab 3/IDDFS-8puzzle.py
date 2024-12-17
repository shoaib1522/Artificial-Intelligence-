def depth_limited_search(current_state, goal_state, depth):
    if current_state == goal_state:
        return []
    if depth == 0:
        return None

    empty_index = current_state.index(0)
    row = empty_index // 3
    col = empty_index % 3
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in directions:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = current_state[:]
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            result = depth_limited_search(new_state, goal_state, depth - 1)
            if result is not None:
                return [new_state] + result

    return None

def iddfs(start_state, goal_state, max_depth):
    for depth in range(max_depth):
        result = depth_limited_search(start_state, goal_state, depth)
        if result is not None:
            return [start_state] + result
    return None

start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = iddfs(start_state, goal_state, 20)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
