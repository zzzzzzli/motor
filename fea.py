import math as m
import numpy as np

def fea(nodes,units):
    for unit in units:
        x = [nodes[n][0] for n in unit]
        y = [nodes[n][1] for n in unit]
        z = [nodes[n][2] for n in unit]
        A = np.([[1,1,1,1],x,y,z])
