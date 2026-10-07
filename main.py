"""A terminal-based, two-player Tic-Tac-Toe game."""


def create_board():
    """Return an empty 3-by-3 game board."""
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Print the board with 0-based row and column coordinates."""
    print("    0   1   2")
    print("  +---+---+---+")
    for row_index, row in enumerate(board):
        print(f"{row_index} | " + " | ".join(row) + " |")
        print("  +---+---+---+")


def has_won(board, mark):
    """Return whether mark occupies a complete row, column, or diagonal."""
    rows = board
    columns = [[board[row][column] for row in range(3)] for column in range(3)]
    diagonals = [
        [board[index][index] for index in range(3)],
        [board[index][2 - index] for index in range(3)],
    ]

    return any(
        all(cell == mark for cell in line)
        for line in rows + columns + diagonals
    )


def get_coordinate(prompt):
    """Read and validate one 0-based board coordinate."""
    while True:
        try:
            coordinate = int(input(prompt))
        except ValueError:
            print("Please enter a whole number from 0 to 2.")
            continue

        if coordinate not in range(3):
            print("That coordinate is out of range. Enter 0, 1, or 2.")
            continue

        return coordinate


def get_move(board, player):
    """Return a valid empty (row, column) selection for the current player."""
    player_number = 1 if player == "X" else 2
    while True:
        row = get_coordinate(
            f"Player {player_number} ({player}), enter a row (0-2): "
        )
        column = get_coordinate(
            f"Player {player_number} ({player}), enter a column (0-2): "
        )

        if board[row][column] != " ":
            print("That space is already occupied. Choose an empty space.")
            continue

        return row, column


def play_game():
    """Run a complete two-player game in the terminal."""
    board = create_board()
    player = "X"
    winner = None

    while True:
        display_board(board)
        row, column = get_move(board, player)
        board[row][column] = player

        if has_won(board, player):
            winner = player
            break

        if all(cell != " " for board_row in board for cell in board_row):
            break

        player = "O" if player == "X" else "X"

    display_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()