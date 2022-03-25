from connectfour import *
from computer import *

DEPTH = 5


def main():
    curr_move = determine_order()
    board = create_board()
    draw_board(board)
    print("It is player %s's turn!" % curr_move)

    while not game_over(board):
        if curr_move == "X":
            slot = player_move(board)
            board = make_move(board, slot, "X")
            curr_move = "O"
        else:
            slot = computer_move(board, DEPTH)
            board = make_move(board, slot, "O")
            print("Computer (O) placed in slot %i" % slot)
            curr_move = "X"
            draw_board(board)
            print("It is player %s's turn!" % curr_move)

    if check_win(board, "X"):
        print("Player (X) Wins!")
    elif check_win(board, "O"):
        print("Computer (O) Wins!")
    elif check_tie(board):
        print("It's a tie!")
    else:
        raise Exception("Exited game loop without game over")


def determine_order() -> str:
    player = input("Who goes first: X (player) or O (computer)?")
    player = player.upper()
    while player != "X" and player != "O":
        player = input("Error: must answer with 'X' or 'O'. Try again:")
        player = player.upper()
    return player


def player_move(board: list) -> int:
    proper_input = False
    slot = int(input("Slot?"))
    while not validate_move(board, slot):
        slot = int(input("Invalid move. Try again:"))
    return slot


if __name__ == '__main__':
    main()
