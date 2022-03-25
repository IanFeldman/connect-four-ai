EMPTY_SLOT = "-"
P1 = "X"
P2 = "O"

HEIGHT = 6
WIDTH = 7


# initializes board
def create_board() -> list:
    board = []
    for j in range(HEIGHT):
        row = []
        for i in range(WIDTH):
            row.append(EMPTY_SLOT)
        board.append(row)
    return board


# draws board to console
def draw_board(board: list) -> None:
    print("  1 2 3 4 5 6 7  ")
    for row in board:
        print("| ", end="")
        for val in row:
            print(val, end=" ")
        print("|")


# checks if a move is valid
def validate_move(board: list, slot: int) -> bool:
    # check slot
    i = slot - 1
    in_range = 0 <= i <= WIDTH - 1
    if not in_range:
        return False

    # check column is not full
    col_full = True
    for col in board:
        if col[i] == EMPTY_SLOT:
            col_full = False
            break
    if col_full:
        return False

    return True


# creates move on the board
def make_move(board: list, slot: int, player: str) -> list:
    new_board = [row[:] for row in board]
    for j in range(HEIGHT):
        i = slot - 1
        val = new_board[j][i]
        # if were at the bottom row
        if val == EMPTY_SLOT and j == HEIGHT - 1:
            new_board[j][i] = player
            return new_board
        # if we've reached a piece
        elif val != EMPTY_SLOT:
            new_board[j - 1][i] = player
            return new_board
    raise Exception("Make move failure")


# checks if a player has won
def check_win(board: list, player: str) -> bool:
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if board[j][i] == player:
                # check up
                if j >= 3 and board[j - 1][i] == board[j - 2][i] == board[j - 3][i] == player:
                    return True
                # check down
                if j < 3 and board[j + 1][i] == board[j + 2][i] == board[j + 3][i] == player:
                    return True
                # check left
                if i >= 3 and board[j][i - 1] == board[j][i - 2] == board[j][i - 3] == player:
                    return True
                # check right
                if i <= 3 and board[j][i + 1] == board[j][i + 2] == board[j][i + 3] == player:
                    return True
                # check diagonal up-right
                if i <= 3 <= j and board[j - 1][i + 1] == board[j - 2][i + 2] == board[j - 3][i + 3] == player:
                    return True
                # check diagonal down-right
                if j < 3 and i <= 3 and board[j + 1][i + 1] == board[j + 2][i + 2] == board[j + 3][i + 3] == player:
                    return True
    return False


# checks for tie
def check_tie(board: list) -> bool:
    board_full = True
    for row in board:
        for val in row:
            if val == EMPTY_SLOT:
                board_full = False
                break
    return board_full


# checks if game over
def game_over(board: list) -> bool:
    x_win = check_win(board, "X")
    o_win = check_win(board, "O")
    tie = check_tie(board)
    return x_win or o_win or tie
