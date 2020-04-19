import numpy as np

def generador(_min, _max):
    return(np.random.randint(_min, _max, size = 64).reshape(4, 16))

ingresos = generador(100, 180)
egresos = generador(60, 130)