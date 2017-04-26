# Create the board
import numpy as np
import random
import time
import matplotlib.pyplot as plt

def create_board():
    return np.array([[0] * 3 for x in range(3)])
board = create_board()

# Place the board
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
board = create_board()
place(board, 1, (0, 0))

# Return the possibilities
def possibilities(board):
    return list(zip(*np.where(board == 0)))
possibilities(board)

# Randomly place
def random_place(board, player):
    select = possibilities(board)
    if len(select) > 0:
        select = random.choice(select)
        place(board, player, select)
    return board
random_place(board, 2)

board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)
print(board)

def row_win(board, player):
    if np.any(np.all(board == player, axis=1)):
        return True
    else:
        return False
        
row_win(board, 1)

def col_win(board, player):
    if np.any(np.all(board == player, axis=1)):
        return True
    else:
        return False
        
col_win(board, 1)

def diag_win(board, player):
    if np.any(np.all(board == player, axis=1)):
        return True
    else:
        return False
        
diag_win(board, 1)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

def play_game():
    board, winner = create_board(), 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
    
play_game()


start = time.time()
games = [play_game() for i in range(1000)]
stop = time.time()
print(stop - start)
plt.hist(games)
plt.show()

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game()  


def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game()  
















