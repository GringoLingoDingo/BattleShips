import random
import numpy as np



def place_pieces(variable):
    y = (int(input("place ship on which row!")))
    x = (int(input("place ship on which column?")))
    
    variable[x][y]= "B"
    print(variable)
    #return variable

