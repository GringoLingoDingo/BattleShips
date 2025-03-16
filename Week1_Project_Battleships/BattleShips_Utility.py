import random
import numpy as np

BOATS_TO_PLACE = 3
SLOOPS_TO_PLACE = 2
FRIGATES_TO_PLACE = 1

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

def computer_pieces_count(Board_H, boats_placed):
    while boats_placed < BOATS_TO_PLACE:
            Board_H = computer_boat_placement(Board_H)
            if boats_placed < SLOOPS_TO_PLACE:
                Board_H = computer_sloop_placement(Board_H)
            if boats_placed < FRIGATES_TO_PLACE:
                Board_H = computer_frigate_placement(Board_H)
            boats_placed += 1


def player_pieces_count(Board_P, boats_placed):
    while boats_placed < BOATS_TO_PLACE:
            Board_P = place_boat(Board_P)
            if boats_placed < SLOOPS_TO_PLACE:
                Board_P = place_sloop(Board_P)
            if boats_placed < FRIGATES_TO_PLACE:
                Board_P = place_frigate(Board_P)
            boats_placed += 1





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
        





def computer_boat_placement(variable):
    for _ in range(100):
        x = random.randint(1,9)
        y = random.randint(1,9)
        orientacion = random.choice(["Horizontal", "Vertical"])
        boat_location = [(x, y)]
        if orientacion == "Horizontal":
            boat_location.append((x, y + 1))
        else:
            boat_location.append((x + 1, y))

        for boat_tiles in boat_location:
            if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
                break
        else:  #maybe this is wrong? do you need an else here??
            for boat_tiles in boat_location:
                variable[boat_tiles] = "B"
            return variable
    return variable


def computer_sloop_placement(variable):
    for _ in range(100):
        x = random.randint(1,8)
        y = random.randint(1,8)
        orientacion = random.choice(["Horizontal", "Vertical"])
        boat_location = [(x, y)]
        if orientacion == "Horizontal":
            boat_location.append((x, y + 1))
            boat_location.append((x, y + 2))
        else:
            boat_location.append((x + 1, y))
            boat_location.append((x + 2, y))
    
        for boat_tiles in boat_location:
            if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
                break
        else:
            for boat_tiles in boat_location:
                variable[boat_tiles] = "S"
            return variable
    return variable



def computer_frigate_placement(variable):
    for _ in range(100):
        x = random.randint(1,7)
        y = random.randint(1,7)
        orientacion = random.choice(["Horizontal", "Vertical"])
        boat_location = [(x, y)]
        if orientacion == "Horizontal":
            boat_location.append((x, y + 1))
            boat_location.append((x, y + 2))
            boat_location.append((x, y + 3))
        else:
            boat_location.append((x + 1, y))
            boat_location.append((x + 2, y))
            boat_location.append((x + 3, y))

        for boat_tiles in boat_location:
            if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
                break
        else:
            for boat_tiles in boat_location:
                variable[boat_tiles] = "F"
            return variable
    return variable


def computer_attack_placement(variable):
    x = random.randint(1,10)
    y = random.randint(1,10)

    if variable [x][y] == "O" or variable [x][y] == "X":
        computer_attack_placement(variable)
    elif variable [x][y] == "B":
         variable [x][y] = "X"
    else:
        variable [x][y] = "O"



def shoot_square(board_seen, board_unseen):
   y = (int(input("Fire at which row!")))
   x = (int(input("Fire at which column?")))

   if board_unseen[x][y] == "B" or board_unseen[x][y] == "S" or board_unseen[x][y] == "F":
         
         board_seen[x][y] = "X"
         print(board_seen)
         # Give point to player
         # Create a boolean that checks if it is already a bonus turn, if so, give another point.
         # Give bonus turn to player
         
   else:
       board_seen[x][y] = "O"
       print(board_seen)
       # Swap over the turns to the other player


def place_boat(variable):
    x = (int(input("place boat on which row!")))
    y = (int(input("place boat on which column?")))

    orientacion = str(input("Do you want it pointing down or to the right? Length 2(d or r)"))

    boat_location = [(x, y)]
    if orientacion == "r":
        boat_location.append((x, y + 1))
    else:
        boat_location.append((x + 1, y))
    
    for boat_tiles in boat_location:
        if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
            break
    else:  #maybe this is wrong? do you need an else here??
        for boat_tiles in boat_location:
            variable[boat_tiles] = "B"
        print(variable)
        return variable






def place_sloop(variable):
    x = (int(input("place ship on which row!")))
    y = (int(input("place ship on which column?")))

    orientacion = str(input("Do you want it pointing down or to the right? Length 3 (d or r)"))

    boat_location = [(x, y)]
    if orientacion == "r":
        boat_location.append((x, y + 1))
        boat_location.append((x, y + 2))
    else:
        boat_location.append((x + 1, y))
        boat_location.append((x + 2, y))

    for boat_tiles in boat_location:
        if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
            break
    else:
        for boat_tiles in boat_location:
            variable[boat_tiles] = "S"
        print(variable)
        return variable







def place_frigate(variable):
    x = (int(input("place ship on which row!")))
    y = (int(input("place ship on which column?")))

    orientacion = str(input("Do you want it pointing down or to the right? Length 4(d or r)"))

    boat_location = [(x, y)]
    if orientacion == "r":
        boat_location.append((x, y + 1))
        boat_location.append((x, y + 2))
    else:
        boat_location.append((x + 1, y))
        boat_location.append((x + 2, y))

    for boat_tiles in boat_location:
        if variable[boat_tiles[0], boat_tiles[1]] in ["B", "S", "F"]:
            break
    else:
        for boat_tiles in boat_location:
            variable[boat_tiles] = "S"
        print(variable)
        return variable








#def check_victory(user, computer):
        # return ('B' not in user) or ('B' not in computer)


def testing_import_of_functions():
    return "This import worked successfully!"

