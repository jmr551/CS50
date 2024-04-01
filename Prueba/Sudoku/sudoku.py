import copy
def create_board():
    board = [ [0] * 9 for _ in range(9) ]
    return board

def print_board(board):
    for row in board:
        print(row)

def play_move(board, position, number):
    row = position [0]
    col = position [1]
    new_board = copy.deepcopy(board)
    new_board[row][col] = number
    return new_board

def free_places(board):
    free = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                free.append((i, j))
    return free


def candidate_numbers(board, position):
    cands = []
    for n in range(1, 10): # es un posible candidato
        # Verifico si no está en la fila
        if n in board[position[0]]:
            continue

        # Verifico si no está en la columna
        for i in range(9):
            if n == board[i][position[1]]:
                continue

        # Verifico si no está en la submatriz 3x3
        in_x = position[0]//3
        in_y = position[1]//3
        for i in range(in_x, in_x + 3):
            for j in range(in_y, in_y + 3):
                if n == board[i][j]:
                    continue

        cands.append(n)
    return cands

def valido(board):
    for i in range(9): #para cada fila
        for j in range(9): # para cada numero de la fila
            if board[i][j] != 0:
                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k]: # misma fila
                        return False

            if board[j][i] != 0:
                for k in range(i + 1, 9):
                    if board[j][i] == board[k][i]: # misma columna
                        return False

            if board[i][j] != 0:
                for k_i in range((i//3)*3, (i//3+1)*3):
                    for k_j in range((j//3)*3, (j//3+1)*3):
                        if i!=k_i and j!= k_j:
                            if board[i][j] == board[k_i][k_j]:
                                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for c in candidate_numbers(board, (i, j)):
                    new_board = play_move(board, (i, j), c)
                    if valido(new_board):
                        if not free_places(board):
                            return new_board
                        else:
                           solve(new_board)

    return None

def create_board_1():
    board = [
        [0, 4, 9, 3, 0, 0, 0, 5, 7],
        [5, 0, 0, 7, 6, 0, 9, 0, 0],
        [0, 2, 7, 0, 5, 0, 6, 1, 0],
        [0, 9, 0, 0, 1, 7, 0, 0, 2],
        [2, 1, 8, 0, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 2, 0, 0, 0, 6],
        [0, 0, 0, 0, 4, 5, 3, 7, 0],
        [0, 0, 4, 0, 9, 0, 0, 0, 1],
        [1, 8, 0, 6, 7, 3, 0, 0, 9]
    ]
    return board


board = create_board_1()
print(solve(board))
