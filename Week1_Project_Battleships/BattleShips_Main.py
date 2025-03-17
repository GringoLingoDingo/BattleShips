import BattleShips_Utility as BSU
import random
import numpy as np

Playername= str(input("Welcome to battleships! What is your name?"))

board_P = BSU.create_board() #Board Player
board_C = BSU.create_board() #Board Computer
board_H = BSU.create_board() #Board Computer Hidden
print(board_P) 
print(board_C)

BOATS_TO_PLACE = 3
SLOOPS_TO_PLACE = 2
FRIGATES_TO_PLACE = 1
starting_boats_PC = 0
starting_boats_CPU = 0
#Total_turns = 30

BSU.computer_pieces_count(board_H, starting_boats_CPU)

BSU.player_pieces_count(board_P, starting_boats_PC)

#This should be  a function you call from Utilities..
for _ in range(80):
    if BSU.no_ships_left(board_P):
        print(f"{Playername} has no ships left! The computer wins!")
        break  
  

    if BSU.no_ships_left(board_H):
        print(f"The computer has no ships left! {Playername} wins!")
        break

    if player_turn:
        BSU.shoot_square(board_C, board_H)
    else:
        BSU.computer_attack_placement(board_P)

    player_turn = not player_turn
    
    

    #Things to add
    #Turn addition if a direct hit occurs
    #Just all around fix your disastrous spaghetti code
    #Use a Class system for the boats,sloops and frigates instead of 3 functions for each (TWICE BTW)
    #Change the win condition to be points based?
    #Place your boats and fire your shots using WASD to move it around your board (I dont think this is possible to figure out without some AI help..)
    #Why are some functions using if == "" and others using "in []"?? cleanup your logic.
