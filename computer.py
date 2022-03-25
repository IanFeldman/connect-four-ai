from connectfour import *


# evaluates board position
# positive for p1 (x), negative for p2 (o)
def eval_board(board: list) -> float:
    score = x_score = o_score = 0.0
    for a in range(2):
        player = "X"
        if a == 1:
            player = "O"
            x_score = score
            score = 0

        for j in range(HEIGHT):
            for i in range(WIDTH):
                if board[j][i] == player:
                    # check up
                    if j >= 3:
                        if board[j - 1][i] == player:
                            score += 1.0
                            if board[j - 2][i] == player:
                                score += 2.0
                                if board[j - 3][i] == player:
                                    score += 3.0
                    # check down
                    if j < 3:
                        if board[j + 1][i] == player:
                            score += 1.0
                            if board[j + 2][i] == player:
                                score += 2.0
                                if board[j + 3][i] == player:
                                    score += 3.0
                    # check left
                    if i >= 3:
                        if board[j][i - 1] == player:
                            score += 1.0
                            if board[j][i - 2] == player:
                                score += 2.0
                                if board[j][i - 3] == player:
                                    score += 3.0
                    # check right
                    if i <= 3:
                        if board[j][i + 1] == player:
                            score += 1.0
                            if board[j][i + 2] == player:
                                score += 2.0
                                if board[j][i + 3] == player:
                                    score += 3.0
                    # check diagonal up-right
                    if i <= 3 <= j:
                        if board[j - 1][i + 1] == player:
                            score += 1.0
                            if board[j - 2][i + 2] == player:
                                score += 2.0
                                if board[j - 3][i + 3] == player:
                                    score += 3.0
                    # check diagonal down-right
                    if j < 3 and i <= 3:
                        if board[j + 1][i + 1] == player:
                            score += 1.0
                            if board[j + 2][i + 2] == player:
                                score += 2.0
                                if board[j + 3][i + 3] == player:
                                    score += 3.0
    o_score = score
    score = x_score - o_score
    return score


# recursive algorithm determining best choices
def minimax(board: list, depth: int, player: str) -> float:
    if depth == 0 or game_over(board):
        return eval_board(board)

    if player == "X":
        max_eval = float("-inf")
        for slot in range(7):
            slot += 1
            if not validate_move(board, slot):
                continue
            possible_board = make_move(board, slot, "X")
            move_eval = minimax(possible_board, depth - 1, "O")
            max_eval = max(move_eval, max_eval)
        return max_eval

    elif player == "O":
        min_eval = float("inf")
        for slot in range(7):
            slot += 1
            if not validate_move(board, slot):
                continue
            possible_board = make_move(board, slot, "O")
            move_eval = minimax(possible_board, depth - 1, "X")
            min_eval = min(move_eval, min_eval)
        return min_eval


# returns best move for computer
def computer_move(board: list, depth: int) -> int:
    min_eval = float("inf")
    best_move = -1
    for slot in range(7):
        slot += 1
        if not validate_move(board, slot):
            continue
        possible_board = make_move(board, slot, "O")
        move_eval = minimax(possible_board, depth - 1, "X")
        if move_eval < min_eval:
            min_eval = move_eval
            best_move = slot

    if best_move == -1:
        raise Exception("Minimax failure")
    return best_move
