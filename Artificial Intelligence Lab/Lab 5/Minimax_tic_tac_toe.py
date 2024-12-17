class Minimax:
    def __init__(self, board):
        self.board = board

    def is_end(self, state):
        for row in state:
            if row[0] == row[1] == row[2] and row[0] != '':
                return True
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] and state[0][col] != '':
                return True
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '':
            return True
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '':
            return True
        if all(cell != '' for row in state for cell in row):
            return True
        return False
    
    def score(self, state):
        for row in state:
            if row[0] == row[1] == row[2] and row[0] != '':
                return 1 if row[0] == 'X' else -1
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] and state[0][col] != '':
                return 1 if state[0][col] == 'X' else -1
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '':
            return 1 if state[0][0] == 'X' else -1
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '':
            return 1 if state[0][2] == 'X' else -1
        return 0
    
    def minimax(self, state, depth, is_max):
        if self.is_end(state):
            return self.score(state)
        
        if is_max:
            max_value = float('-inf')
            for move in self.get_moves(state):
                result = self.minimax(self.make_move(state, move, 'X'), depth+1, False)
                max_value = max(max_value, result)
            return max_value
        else:
            min_value = float('inf')
            for move in self.get_moves(state):
                result = self.minimax(self.make_move(state, move, 'O'), depth+1, True)
                min_value = min(min_value, result)
            return min_value
    
    def get_moves(self, state):
        moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == '':
                    moves.append((i, j))
        return moves

    def make_move(self, state, move, player):
        new_state = [row[:] for row in state]
        new_state[move[0]][move[1]] = player
        return new_state

    def find_best(self, state):
        best = None
        best_value = float('-inf')
        for move in self.get_moves(state):
            new_state = self.make_move(state, move, 'X')
            move_value = self.minimax(new_state, 0, False)
            if move_value > best_value:
                best_value = move_value
                best = move
        return best

game_state = [['X', 'O', 'X'], 
              ['O', 'X', ''], 
              ['', '', 'O']]

minimax = Minimax(game_state)
best_move = minimax.find_best(game_state)
print("Best move for 'X':", best_move)
