print("--------------------TIC TAC TOE--------------------")
# creates the board
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" | ")
        print("\n" + "-" * 13)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
      #  checking for a win in either a row or a column
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check for a win (diagonals)
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def initialize_board():
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(' ')
        board.append(row)
    return board

def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play_tic_tac_toe()