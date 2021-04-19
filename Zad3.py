import numpy as np
import math

def tablica(x):
    h = math.pow(x,2)
    a = np.arange(1, h+1).reshape(x, x)
    return a

print(tablica(9))
