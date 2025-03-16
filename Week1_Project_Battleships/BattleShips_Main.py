import BattleShips_Utility as BSU
import random
import numpy as np

Playername= str(input("Welcome to battleships! What is your name?"))

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
#Total_turns = 30

BSU.computer_pieces_count(board_H, starting_boats_CPU)
print(board_H)

BSU.player_pieces_count(board_P, starting_boats_PC)

for _ in range(40):
    if BSU.no_ships_left(board_P):
        print(f"{Playername} has no ships left! The computer wins!")
        break  
    else:
        BSU.shoot_square(board_C, board_H)

    if BSU.no_ships_left(board_H):
        print(f"The computer has no ships left! {Playername} wins!")
        break
    else:
        BSU.computer_attack_placement(board_P)