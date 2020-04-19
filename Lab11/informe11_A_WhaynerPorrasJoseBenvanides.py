import numpy as np

def generador(_min, _max):
    return(np.random.randint(_min, _max, size = 64).reshape(4, 16))

