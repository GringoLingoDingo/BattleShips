import BattleShips_Utility as BSU

import numpy as np

board_P = BSU.create_board()
board_C = BSU.create_board()
board_H = BSU.create_board()
print(board_P) 
print(board_C)

BOATS_TO_PLACE = 3
SLOOPS_TO_PLACE = 2
FRIGATES_TO_PLACE = 1
starting_boats_PC = 0
starting_boats_CPU = 0

BSU.computer_pieces_count(board_H, starting_boats_CPU)
print(board_H)

BSU.player_pieces_count(board_P, starting_boats_PC)

