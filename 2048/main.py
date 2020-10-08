#Input: The input is always a valid game state of a 2048 puzzle. The first four lines of input, that each contains four integers, describe the 16 integers in the 4 \times 4 grid of 2048 puzzle. The j-th integer in the i-th line denotes the content of the cell located at the i-th row and the j-th cell. For this problem, all integers in the input will be either {0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}. Integer 0 means an empty cell.The fifth line of input contains an integer 0, 1, 2, or 3 that denotes a left, up, right, or down move executed by the player, respectively.

#Output: Output four lines with four integers each. Two integers in a line must be separated by a single space. This describes the new state of the 4 \times 4 grid of 2048 puzzle. Again, integer 0 means an empty cell. Note that in this problem, you can ignore the part from the 2048 puzzle where it introduces a new random tile with a value of either 2 or 4 in an empty spot of the board at the start of a new turn.

import sys

board = [[int(e) for e in sys.stdin.readline().split()] for _ in range(4)]
dir = int(sys.stdin.readline())

def flip_horizontal():
    global board
    for r, row in enumerate(board):
        board[r] = row[::-1]

def flip_diagonal():
    global board
    board[0][0], board[3][3] = board[3][3], board[0][0]
    board[0][1], board[2][3] = board[2][3], board[0][1]
    board[0][2], board[1][3] = board[1][3], board[0][2]
    board[1][0], board[3][2] = board[3][2], board[1][0]
    board[1][1], board[2][2] = board[2][2], board[1][1]
    board[2][0], board[3][1] = board[3][1], board[2][0]
    
def rotate_cw():
    for _ in range(3):
        flip_diagonal()
        flip_horizontal()

def rotate_ccw():
    flip_diagonal()
    flip_horizontal()

def step(list):
    res = []

    # remove zeros
    list = [e for e in list if e]

    while list:
        if len(list) > 1:
            if list[0] == list[1]:
                res.append(list[0]*2)
                list = list[2:]
            else:
                res.append(list[0])
                list = list[1:]
        else:
            res.append(list[0])
            list = list[1:]

    return res + [0]*(4-len(res))

def solve():
    global board
    new_board = []
    for row in board:
        new_board.append(step(row))
    board = new_board

if dir == 0:
    solve()

if dir == 1:
    rotate_ccw()
    solve()
    rotate_cw()

if dir == 2:
    rotate_ccw()
    rotate_ccw()
    solve()
    rotate_ccw()
    rotate_ccw()

if dir == 3:
    rotate_cw()
    solve()
    rotate_ccw()

# print result
for row in board:
    print(*row)