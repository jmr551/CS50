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
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
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
    if player(board) == X: # Queremos MAXimizar
        value, action = max_value(board)
    else:
        value, action = min_value(board)
    return action

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float("inf")
    best_action = None
    for action in actions(board):
        value, _ = max_value(result(board, action))
        if value < v:
            v = value
            best_action = action
    return v, best_action


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float("-inf")
    best_action = None
    for action in actions(board):
        value, _ = min_value(result(board, action))
        if value > v:
            v = value
            best_action = action
    return v, best_action


def print_tab(board):
    for i in range(3):
        print(board[i])
    print("")

def compare_moves(actual_move, expected_move):
    if actual_move == expected_move:
        print(f"Resultado correcto: {actual_move}")
    else:
        print(f"Resultado incorrecto: {actual_move}, se esperaba: {expected_move}")

def main():
    # Caso de prueba 1: Tablero vacío (la jugada esperada puede variar ya que todas son igualmente válidas)
    print("Caso de prueba 1: Tablero vacío")
    b = initial_state()
    print_tab(b)
    move = minimax(b)
    # Para este caso, no especificamos una jugada esperada ya que cualquier primera jugada es válida.
    print("Mejor movimiento: ", move)

    print("\nCaso de prueba 2 corregido: X está a punto de ganar")
    b = [[X, O, O],
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    print_tab(b)
    move = minimax(b)
    compare_moves(move, (2, 0))  # Esperamos que X complete su línea y gane en (2, 0)


    # Caso de prueba 3: O está a punto de ganar
    print("\nCaso de prueba 3: O está a punto de ganar")
    b = [[O, X, X],
         [X, O, EMPTY],
         [EMPTY, EMPTY, EMPTY]]
    print_tab(b)
    move = minimax(b)
    compare_moves(move, (2, 2))  # Esperamos que O complete su línea en (2, 2)

    # Caso de prueba 4: Bloquear a X de ganar
    print("\nCaso de prueba 4: Bloquear a X de ganar")
    b = [[X, EMPTY, EMPTY],
         [O, X, EMPTY],
         [EMPTY, O, EMPTY]]
    print_tab(b)
    move = minimax(b)
    compare_moves(move, (2, 2))  # Esperamos que O bloquee a X en (2, 2)

    # Caso de prueba 5: Solo queda un movimiento
    print("\nCaso de prueba 5: Solo queda un movimiento")
    b = [[X, O, X],
         [X, O, O],
         [O, X, EMPTY]]
    print_tab(b)
    move = minimax(b)
    compare_moves(move, (2, 2))  # El único movimiento restante

    # Caso de prueba 6: Tablero que lleva a un empate
    print("\nCaso de prueba 6: Tablero que lleva a un empate")
    b = [[X, O, X],
         [X, EMPTY, O],
         [O, X, EMPTY]]
    print_tab(b)
    move = minimax(b)
    # En este caso, puede haber más de una jugada "correcta" que lleve a un empate.
    print("Mejor movimiento: ", move)

    # Añade más casos de prueba según lo veas necesario.

if __name__ == "__main__":
    main()
