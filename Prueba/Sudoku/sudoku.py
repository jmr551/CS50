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
            next

        # Verifico si no está en la columna
        for i in range(9):
            if n in board[i][position[1]]:
                next

        # Verifico si no está en la submatriz 3x3
        in_x = position[0]//3
        in_y = position[1]//3
        for i in range(in_x, in_x + 3):
            for j in range(in_y, in_y + 3):
                if n == board[i][j]:
                    next

        cands.append(n)
    return cands

def valido(board):
    

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for c in candidate_numbers(board, (i, j)):



board = create_board()
print_board(board)
board = play_move(board, (0, 0), 1)
print_board(board)
