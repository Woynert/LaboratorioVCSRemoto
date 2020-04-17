#include <iostream>
#include <stdlib.h>
#include <stdio.h>      /* printf */
#include <math.h>       /* floor */
#include <bits/stdc++.h> 
#include <string>

/*
Integrantes del grupo:
- Whayner Eduardo Porras Rodriguez
- José Santiago Benavides Céspedes
*/

using namespace std;

//Mapa del videojuego
//El 1 Representa una pared y el 0 Representa un espacio vacio
int player[2] = {2, 2};
int mapa[5][5] = {
    {1, 1, 1, 1, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 1, 1, 1, 1}};
string txt = "";

//Dibujar el mapa en la pantalla usando for
int drawMap(){
	for (int i = 0; i < 5; i++){
		for (int j = 0; j < 5; j++){
			txt = "";
			if (i == player[1] and j == player[0]) //jugador
                cout << "P ";
            else if (mapa[i][ j] == 0) //espacio
                cout << "  ";
            else if (mapa[i][ j] == 1) //pared
                cout << "# ";
		}
		cout << endl;
	}
}
        
int main(){
	
	drawMap();
	//Controles desde consola
	while(true){
		int mover = 0;
		cout << "1 - Derecha\n2 - Izquierda\n--> " << endl;
	  	cin >> mover;
	    cout << endl;
	    //derecha
	    if (mover == 1)
	        if (mapa[player[0]+1][ player[1]] != 1)
	            player[0] += 1;
	    //izquierda
	    else if (mover == 2)
	        if (mapa[player[0]-1][ player[1]] != 1)
	            player[0] -= 1;
	            
	    //redibujar el mapa
	    drawMap();
	}
}

