# Santino Pineda
# Multidimensional Lists — Tic-Tac-Toe
# A two-player terminal Tic-Tac-Toe game using a 3x3 2D list.

gameBoard = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def print_gameboard(gameboard):
    print("\n    0   1   2")
    print("  +---+---+---+")

    for row in range(len(gameboard)):
        print(f"{row} | {gameboard[row][0]} | {gameboard[row][1]} | {gameboard[row][2]} |")
        print("  +---+---+---+")


def check_winner(gameboard, symbol):
    # Check rows
    for row in range(3):
        if gameboard[row][0] == symbol and gameboard[row][1] == symbol and gameboard[row][2] == symbol:
            return True

    # Check columns
    for col in range(3):
        if gameboard[0][col] == symbol and gameboard[1][col] == symbol and gameboard[2][col] == symbol:
            return True

    # Check top-left to bottom-right diagonal
    if gameboard[0][0] == symbol and gameboard[1][1] == symbol and gameboard[2][2] == symbol:
        return True

    # Check top-right to bottom-left diagonal
    if gameboard[0][2] == symbol and gameboard[1][1] == symbol and gameboard[2][0] == symbol:
        return True

    return False


def check_tied(gameboard):
    for row in range(3):
        for col in range(3):
            if gameboard[row][col] == " ":
                return False

    return True


def make_move(gameboard, name, symbol):
    while True:
        try:
            row = int(input(f"{name}, enter a row (0-2): "))
            col = int(input(f"{name}, enter a column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter whole numbers.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid coordinates. Row and column must be from 0 to 2.")
            continue

        if gameboard[row][col] != " ":
            print("That space is already taken. Choose another space.")
            continue

        gameboard[row][col] = symbol
        break


if __name__ == '__main__':
    print("Ready for a game of Tic-Tac-Toe?")

    playerOneName = input("Please input the name for player one: ")
    playerOneSymbol = "X"

    playerTwoName = input("Please input the name for player two: ")
    playerTwoSymbol = "O"

    currentPlayerName = playerOneName
    currentPlayerSymbol = playerOneSymbol

    gameLoop = "continue"

    print_gameboard(gameBoard)

    while gameLoop == "continue":
        make_move(gameBoard, currentPlayerName, currentPlayerSymbol)

        print_gameboard(gameBoard)

        if check_winner(gameBoard, currentPlayerSymbol):
            print(f"\n{currentPlayerName} wins!")
            gameLoop = "end"
        elif check_tied(gameBoard):
            print("\nThe game is a tie!")
            gameLoop = "end"
        else:
            if currentPlayerSymbol == playerOneSymbol:
                currentPlayerName = playerTwoName
                currentPlayerSymbol = playerTwoSymbol
            else:
                currentPlayerName = playerOneName
                currentPlayerSymbol = playerOneSymbol
