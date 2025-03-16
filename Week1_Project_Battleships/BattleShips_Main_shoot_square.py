from BattleShips_Utility_shoot_square import shoot_square
import numpy as np

def create_board(size=(11, 11)):
    # Initialize an 11x11 board with underscores
    board = np.full(size, '_') 
    
    # Add column labels (top edge: 1-10)
    board[0, 1:] = [str(i) for i in range(1, 11)]
    
    # Add row labels (left edge: 1-10)
    board[1:, 0] = [str(i) for i in range(1, 11)]
    
    board[0, 0] = ' '
    board[10,0] = '0'
    board[0,10] = '0'
    
    return board

board_1 = create_board()

shoot_square(board_1)
print(board_1)