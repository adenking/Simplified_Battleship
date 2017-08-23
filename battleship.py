from random import randint

board = []
for i in range(5):
    board.append(["O"] * 5)


def print_board(board_in):
    for row in board_in:
        print(" ".join(row))


def random_row(board_in):
    return (randint(0, len(board_in) - 1))


def random_col(board_in):
    return randint(0, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
    else:
        if guess_row >= len(board) or guess_col >= len(board[0]):  # TODO add exception handling
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[int(guess_col)][int(guess_row)] = "X"
        print('Turn: {0}'.format(turn + 1))
        print_board(board)
