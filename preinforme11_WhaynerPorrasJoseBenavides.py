import numpy as np 

"""
Integrantes del grupo:
- Whayner Eduardo Porras Rodriguez
- José Santiago Benavides Céspedes
"""

#Mapa del videojuego
#El 1 Representa una pared y el 0 Representa un espacio vacio
player = np.array([2, 2])
mapa = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],])

#Dibujar el mapa en la pantalla usando for
def drawMap():
    for i in range(0, 5):
        txt = ""
        for j in range(0, 5):
            if i == player[1] and j == player[0]: #jugador
                txt += "@ "
            elif (mapa[i, j] == 0): #espacio
                txt += "  "
            elif (mapa[i, j] == 1): #pared
                txt += "█ "
        print(txt)
        
drawMap()
#Controles desde consola
while(True):
    mover = int(input("1 - Derecha\n2 - Izquierda\n--> "))
    
    #derecha
    if mover == 1: 
        if mapa[player[0]+1, player[1]] != 1:
            player[0] += 1
    #izquierda
    elif mover == 2: 
        if mapa[player[0]-1, player[1]] != 1:
            player[0] -= 1
            
    #redibujar el mapa
    drawMap()

