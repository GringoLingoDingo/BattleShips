import random
import numpy as np

def shoot_square(board):
   y = (int(input("Fire at which row!")))
   x = (int(input("Fire at which column?")))

   if board[y][x] == "B":
         
         board[y][x] = "X"
         print(board)
         # Give point to player
         # Create a boolean that checks if it is already a bonus turn, if so, give another point.
         # Give bonus turn to player
         
   else:
       board[y][x] = "O"
       print(board)
       # Swap over the turns to the other player