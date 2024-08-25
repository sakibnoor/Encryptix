import math

# Initialize the board as an empty list with 9 spaces
board = [' ' for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board, show_numbers=False):
    # If show_numbers is True, display positions instead of the board values
    if show_numbers:
        numbered_board = [str(i + 1) for i in range(9)]
        for row in [numbered_board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    else:
        for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

# Check for available moves (empty spaces)
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Check if a player has won the game
def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Check if the game is a draw (no spaces left)
def is_draw(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning to find the optimal move for AI
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    # Check if any player has won
    if is_winner(board, 'O'):
        return 1  # AI wins
    elif is_winner(board, 'X'):
        return -1  # Human wins
    elif is_draw(board):
        return 0  # It's a draw
    
    if is_maximizing:
        # AI is maximizing player
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '  # Undo move
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Prune the search
        return best_score
    else:
        # Human is minimizing player
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '  # Undo move
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Prune the search
        return best_score

# Function to find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for available in available_moves(board):
        board[available] = 'O'  # AI makes a move
        score = minimax(board, 0, False)
        board[available] = ' '  # Undo the move
        if score > best_score:
            best_score = score
            move = available
    return move

# Main game loop
def play_game():
    human = 'X'
    ai = 'O'
    
    print("Welcome to Tic-Tac-Toe!")
    
    # Show numbered board at the start to help the player
    print("\nHere are the numbers corresponding to the board positions:")
    print_board(board, show_numbers=True)

    while True:
        # Human's turn
        print("\nCurrent Board:")
        print_board(board)
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] == ' ':
            board[human_move] = human
        else:
            print("Invalid move, try again.")
            continue
        
        # Check for a winner or a draw
        if is_winner(board, human):
            print_board(board)
            print("You win!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = ai
        print_board(board)
        
        # Check for a winner or a draw
        if is_winner(board, ai):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
