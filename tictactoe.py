"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if any(None in row for row in board):
        O_Count = sum(row.count("O") for row in board)
        X_Count = sum(row.count("X") for row in board)

        if O_Count == X_Count:
            return "X"
        else:
            return "O"
    else:
        return

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    x = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x.add((i,j))
    return x


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        player_turns = player(board)
        next_board = copy.deepcopy(board)
        next_board[i][j] = player_turns
        return next_board
    else:
        raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return "O"
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return "X"
    if board[0][2] == board[1][1] == board[2][0] == "O":
        return "O"
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any(None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":
        best_value = -1
        best_move = (-1,-1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_value = minvalue(result(board, action))
            if move_value == 1:
                best_move = action
                break
            if move_value > best_value:
                best_move = action
        return best_move

    if player(board) == "O":
        best_value = 1
        best_move = (-1,-1)
        for action in actions(board):
            move_value = maxvalue(result(board,action))
            if move_value == -1:
                best_move = action
                break
            if move_value < best_value:
                best_move = action
        return best_move

def maxvalue(board):
    if terminal(board):
        return utility(board)
    mvalue = -1
    for action in actions(board):
        mvalue = max(mvalue, minvalue(result(board,action)))
        if mvalue == 1:
            break
    return mvalue

def minvalue(board):
    if terminal(board):
        return utility(board)
    mvalue = 1
    for action in actions(board):
        mvalue = min(mvalue, maxvalue(result(board,action)))
        if mvalue == -1:
            break
    return mvalue



