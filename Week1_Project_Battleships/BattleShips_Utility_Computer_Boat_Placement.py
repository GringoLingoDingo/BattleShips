import random
import numpy as np

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


