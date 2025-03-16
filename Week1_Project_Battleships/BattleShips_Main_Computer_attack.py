from BattleShips_Utility_Computer_attack import computer_attack_placement
import random 
import numpy as np

def create_board(size=(11, 11)):
    # Initialize an 11x11 board with underscores
    board = np.full(size, '_') 
    
    # Add column labels (top edge: 1-10)
    board[0, 1:] = [str(i) for i in range(1, 11)]
    
    # Add row labels (left edge: 1-10)
    board[1:, 0] = [str(i) for i in range(1, 11)]
    
    # Clear the top-left corner (0,0) for alignment
    board[0, 0] = ' '
    board[10,0] = '0'
    board[0,10] = '0'
    
    return board

board = create_board()

computer_attack_placement(board)

print(board)