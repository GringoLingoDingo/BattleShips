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