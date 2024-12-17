class AlphaBetaPruningAI:
    def __init__(self, search_depth, initial_board, current_player):
        self.search_depth = search_depth
        self.initial_board = initial_board
        self.current_player = current_player
        self.node_count = 0  
        self.evaluated_nodes = []  

    def is_game_over(self, board):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != None:
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != None:
                return True
        if board[0][0] == board[1][1] == board[2][2] != None:
            return True
        if board[0][2] == board[1][1] == board[2][0] != None:
            return True
        for row in board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def calculate_utility(self, board):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != None:
                if board[row][0] == 'X':
                    return 1
                else:
                    return -1
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != None:
                if board[0][col] == 'X':
                    return 1
                else:
                    return -1
        if board[0][0] == board[1][1] == board[2][2] != None:
            if board[0][0] == 'X':
                return 1
            else:
                return -1
        if board[0][2] == board[1][1] == board[2][0] != None:
            if board[0][2] == 'X':
                return 1
            else:
                return -1
        return 0

    def alphabeta(self, board, depth, alpha_value, beta_value, is_maximizing_player):
        self.node_count += 1  
        self.evaluated_nodes.append([row[:] for row in board])
        
        if depth == 0 or self.is_game_over(board):
            return self.calculate_utility(board)
        
        if is_maximizing_player:
            max_evaluation = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        board[row][col] = 'X'
                        evaluation = self.alphabeta(board, depth - 1, alpha_value, beta_value, False)
                        board[row][col] = None
                        max_evaluation = max(max_evaluation, evaluation)
                        alpha_value = max(alpha_value, evaluation)
                        if beta_value <= alpha_value:
                            break
            return max_evaluation
        else:
            min_evaluation = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        board[row][col] = 'O'
                        evaluation = self.alphabeta(board, depth - 1, alpha_value, beta_value, True)
                        board[row][col] = None
                        min_evaluation = min(min_evaluation, evaluation)
                        beta_value = min(beta_value, evaluation)
                        if beta_value <= alpha_value:
                            break
            return min_evaluation

    def select_best_move(self, board):
        self.node_count = 0  # Reset node count for each new move
        self.evaluated_nodes = []  # Reset evaluated nodes for each move
        optimal_value = float('-inf')
        chosen_move = None
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    move_value = self.alphabeta(board, self.search_depth, float('-inf'), float('inf'), False)
                    board[row][col] = None
                    if move_value > optimal_value:
                        optimal_value = move_value
                        chosen_move = (row, col)
        return chosen_move

def print_board(board):
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
    print("-" * 9)

def is_full(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True

def main():
    initial_board_state = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    ai_player = AlphaBetaPruningAI(search_depth=3, initial_board=initial_board_state, current_player='X')

    current_turn = 'X'  
    while not ai_player.is_game_over(initial_board_state) and not is_full(initial_board_state):
        print("Current Board State:")
        print_board(initial_board_state)
        
        if current_turn == 'X':
            print("AI is making a move...")
            ai_player.node_count = 0 
            
            best_move_position = ai_player.select_best_move(initial_board_state)
            
            if best_move_position:
                row, col = best_move_position
                initial_board_state[row][col] = 'X'
                print(f"AI places 'X' at position ({row}, {col})")
                print(f"Total nodes evaluated for this move: {ai_player.node_count}")
                
                print("\nNodes evaluated during this move:")
                for i, node in enumerate(ai_player.evaluated_nodes):
                    print(f"Node {i + 1}:")
                    print_board(node)
            
            current_turn = 'O'
        else:
            print("Human player's turn (O):")
            while True:
                try:
                    row = int(input("Enter the row (0, 1, or 2): "))
                    col = int(input("Enter the column (0, 1, or 2): "))
                    if initial_board_state[row][col] is None:
                        initial_board_state[row][col] = 'O'
                        break
                    else:
                        print("Position is already taken. Choose another.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter numbers between 0 and 2.")
            current_turn = 'X'

    print("Final Board State:")
    print_board(initial_board_state)
    if ai_player.is_game_over(initial_board_state):
        result = ai_player.calculate_utility(initial_board_state)
        if result == 1:
            print("AI (X) wins!")
        elif result == -1:
            print("Human player (O) wins!")
        else:
            print("It's a draw!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
