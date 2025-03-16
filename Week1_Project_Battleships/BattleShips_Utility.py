import random
import numpy as np

BOATS_TO_PLACE = 3
SLOOPS_TO_PLACE = 2
FRIGATES_TO_PLACE = 1

class Gamehandler():
    global BOATS_TO_PLACE

    def __init__(self):
        self.Board_1 = create_board()
        self.Board_2 = create_board()
        self.Board_3 = create_board()
        self.boats_placed = 0
        while self.boats_placed < BOATS_TO_PLACE:
            self.Board_3 = computer_boat_placement(self.Board_3)
            if self.boats_placed < SLOOPS_TO_PLACE:
                self.Board_3 = computer_sloop_placement(self.Board_3)
            if self.boats_placed < FRIGATES_TO_PLACE:
                self.Board_3 = computer_frigate_placement(self.Board_3)
            self.boats_placed += 1
        print(self.Board_3)
        
O = Gamehandler()


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


def computer_boat_placement(variable):
    x = random.randint(1,9)
    y = random.randint(1,9)
    orientacion = random.choice(["Horizontal", "Vertical"])
    boat_location = [(x, y)]
    if orientacion == "Horizontal":
        boat_location.append((x, y + 1))
    else:
        boat_location.append((x + 1, y))
    
    for boat_tiles in boat_location:
        if ([boat_tiles]) == "B":
            computer_boat_placement(variable)
    else:  #maybe this is wrong? do you need an else here??
        for boat_tiles in boat_location:
            variable[boat_tiles] = "B"


def computer_sloop_placement(variable):
    x = random.randint(1,8)
    y = random.randint(1,8)
    orientacion = random.choice(["Horizontal", "Vertical"])
    boat_location = [(x, y)]
    if orientacion == "Horizontal":
        boat_location.append((x, y + 2))
    else:
        boat_location.append((x + 2, y))

    for boat_tiles in boat_location:
        if ([boat_tiles]) == "B":
            computer_boat_placement(variable)
    else:
        for boat_tiles in boat_location:
            variable[boat_tiles] = "B"



def computer_frigate_placement(variable):
    x = random.randint(1,7)
    y = random.randint(1,7)
    orientacion = random.choice(["Horizontal", "Vertical"])
    boat_location = [(x, y)]
    if orientacion == "Horizontal":
        boat_location.append((x, y + 3))
    else:
        boat_location.append((x + 3, y))
        
    for boat_tiles in boat_location:
        if ([boat_tiles]) == "B":
            computer_boat_placement(variable)
    else:
        for boat_tiles in boat_location:
            variable[boat_tiles] = "B"



def computer_attack_placement(variable):
    x = random.randint(1,10)
    y = random.randint(1,10)

    if variable [x][y] == "O" or variable [x][y] == "X":
        computer_attack_placement(variable)
    elif variable [x][y] == "B":
         variable [x][y] = "X"
    else:
        variable [x][y] = "O"



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

def place_pieces(variable):
    y = (int(input("place ship on which row!")))
    x = (int(input("place ship on which column?")))
    
    #tile = [(x,y)]
    variable[x][y]= "B"
    return variable


#def check_victory(user, computer):
        # return ('B' not in user) or ('B' not in computer)


def testing_import_of_functions():
    return "This import worked successfully!"

