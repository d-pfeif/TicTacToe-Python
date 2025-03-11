def print_board(board):
    print("\n TicTacToe Board")
    for index, row in enumerate(board):
        print(" | ".join(row))
        if index < 2:
            print("-" * 10)
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (1, 2, 3): ")) - 1
        col = int(input(f"Player {current_player}, enter the column (1, 2, 3): ")) - 1

        if board[row][col] != " ":
            print("Cell already taken, try again.\n")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!\n")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!\n")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()