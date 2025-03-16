import random
import numpy as np

def computer_attack_placement(variable):
    x = random.randint(1,10)
    y = random.randint(1,10)

    if variable [x][y] == "O" or variable [x][y] == "X":
        computer_attack_placement(variable)
    elif variable [x][y] == "B":
         variable [x][y] = "X"
    else:
        variable [x][y] = "O"
