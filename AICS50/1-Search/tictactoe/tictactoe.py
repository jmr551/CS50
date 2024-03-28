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
    x = 0;
    o = 0;
    empty = 0;
    for row in board:
        for st in row:
            if st == X:
                x += 1
            elif st == O:
                o += 1
            else:
                empty+=1
    if empty == 0:
        return None
    elif x > o:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY or action is None:
        raise ValueError("Action is not valid")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # print(f"Dentro del {i}: {board[i][0]}, {board[i][0]}, {board[i][0]}")
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != None:
                return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != None:
                return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2]!= None:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or player(board) == None:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            win =  board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            win = board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        win = board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        win = board[0][2]
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # board: tablero sin jugar
    if terminal(board):
        return None
    to_play = player(board) # Ahora juega A
    if to_play == X: # Si X-> max, O->min
        ut = -2
    else:
        ut = 2

    for actionA in actions(board):
        board1 = result(board, actionA) #tablero resultante de que A haya jugado (ahora le toca a B)
        if terminal(board1):
            if ((to_play == X and utility(board1) > ut) or (to_play == O and utility(board1) < ut)):
                ut = utility(board1)
                best_action_A = action
        else: #Ahora le toca a B, y B quiere lo opuesto a A
            act2 = minimax(board1) # Obtenemos la mejor acción de B
            board2 = result(board1, act2) # B juega su mejor opción y le toca a A
            if terminated(board2):
                #Se terminó, qué hago en este caso?
                utility(board2)
            act3 = minimax(board2)
            board3 = result(board2, act3)
            ut3 = utility(board3)
            if (to_play == X and ut3 > ut) or (to_play == O and ut3 < ut):
                best_action = act2
                ut = ut2
    return best_action_A
def print_tab(board):
    for i in range(3):
        print(board[i])
    print("")

def main():
    b = initial_state()
    b = result(b,(1, 1))
    b = result(b,(2, 1))
    b = result(b,(0, 0))
    # b = result(b,(2, 2))
    #b = result(b,(1, 0))
    print_tab(b)
    #print(winner(b))
    #print(terminal(b))
    print(minimax(b))
    #b = result(b,(2, 0))
    #
    #print (b)
    #print(utility(b))

    #print (minimax(b))
    # b = result(b,(1, 0))

    # print(minimax([[X,,],[,,],[,,]]))

if __name__ == "__main__":
    main()
