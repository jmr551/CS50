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
    x = 0
    o = 0
    empty = 0
    for row in board:
        for st in row:
            if st == X:
                x += 1
            elif st == O:
                o += 1
            else:
                empty += 1
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
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError("Move is out of bounds")

    if board[action[0]][action[1]] is not None:
        raise ValueError("Move is not allowed; position already taken")

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
    # Asume que `winner` retorna 'X' si X gana, 'O' si O gana, y None si no hay ganador.
    win = winner(board)
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
    if player(board) == X:
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
        result_board = result(board, action)
        value, _ = max_value(result_board)
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
        result_board = result(board, action)
        new_v, _ = min_value(result_board)
        if new_v > v:
            v = new_v
            best_action = action
    return v, best_action


def print_tab(board):
    for i in range(3):
        print(board[i])
    print("")


def print_board(board):
    """Imprime el tablero de juego."""
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 9)


def human_move(board, player):
    """Permite al jugador humano hacer una jugada."""
    print(f"Jugador {player}, es tu turno.")
    available_actions = actions(board)
    while True:
        try:
            row = int(input("Elige la fila (0, 1, 2): "))
            col = int(input("Elige la columna (0, 1, 2): "))
            if (row, col) in available_actions:
                return (row, col)
            else:
                print("Esa jugada no está disponible. Por favor, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números.")


def main():
    board = initial_state()
    print("Bienvenido al Tic Tac Toe!")
    user_player = input("¿Quieres ser X o O? ").upper()
    if user_player not in ["X", "O"]:
        user_player = "X"
        print("Selección inválida. Serás X por defecto.")
    ai_player = "O" if user_player == "X" else "X"

    current_player = "X"  # X siempre inicia
    while not terminal(board):
        print_board(board)
        if current_player == user_player:
            move = human_move(board, user_player)
        else:
            print("Turno del algoritmo Minimax...")
            move = minimax(board)
            if move is None:  # Si minimax no puede hacer una jugada (tablero lleno)
                break
            print(f"Minimax ({ai_player}) juega en la fila {move[0]}, columna {move[1]}")
        board = result(board, move)
        current_player = "O" if current_player == "X" else "X"  # Cambiar de jugador

    print_board(board)
    if winner(board) is None:
        print("¡Es un empate!")
    else:
        print(f"El ganador es {winner(board)}!")


if __name__ == "__main__":
    main()
