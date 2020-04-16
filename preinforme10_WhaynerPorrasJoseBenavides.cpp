#include <iostream>
#include <stdlib.h>
#include <stdio.h>      /* printf */
#include <math.h>       /* floor */
#include <bits/stdc++.h> 

/*
Integrantes del grupo:
- Whayner Eduardo Porras Rodriguez
- José Santiago Benavides Céspedes
*/

using namespace std;

//variables
int util[] = {
27834, //0
23789, //1
30189,
30967,
32501,
32701,
31665,
17155,
4614, //8
834}; //9

//1. Diferencia - media -> últimos dos años / primeros dos años
float difMedia(){
	float media = abs(((util[0] + util[1]) / 2) - ((util[8] + util[9]) / 2));
	return(media);
}

//2. Diferencia -> año con mayor utilidad / año con menor utilidad
float difMayMenUti(){
	int may = 0;
	int men = 100000;
	int length = sizeof(util)/sizeof(util[0]);
	for(int i = 0; i < length; i++){
		if (util[i] > may){
			may = util[i];
		}
		else if (util[i] < men){
			men = util[i];
		}
	}
	
	return(may-men);
}

//3. Mediana
float mediana(){
	int length = sizeof(util)/sizeof(util[0]);
	int mediana = 0;
	
	//organizarlos de mayor a menor
	int size = sizeof(util) / sizeof(util[0]);
	sort(util, util +size);
	
	//par
	if (length % 2 == 0){
		mediana = ( util[length/2] + util[(length/2)+1] ) / 2;
	}
	else{ //impar
		mediana = util[int(floor(length/2 + 1/2))];
	}
	
	return(mediana);
}

//4. Diferencia -> Media / Mediana
int difMediaMediana(){
	
	//total
	int acu = 0;
	int size = sizeof(util) / sizeof(util[0]);
	for(int i = 0; i < size; i++){
		acu += util[i];
	}
	
	int media = acu/size;
	int median = mediana();
	
	int dif = abs(media-median);
	return(dif);
}

//5. Porcentaje por valor
void porApo(){
	
	//obtener total
	int acu = 0;
	int size = sizeof(util) / sizeof(util[0]);
	for(int i = 0; i < size; i++){
		acu += util[i];
	}
	
	//comparar
	for(int i = 0; i < size; i++){
		float val = (util[i]*100.0)/acu;
		cout << i+2008 << " -> " << val << "%" << endl;
	}
	
}

//6. Deficit del 2017 con respecto al 2016
int deficit20172016(){
	return(abs(util[9] - util[8]));
}

//7. Porcentaje deficit por año
void porDef(){
	
	//obtener tamaño
	int size = sizeof(util) / sizeof(util[0]);
	
	//comparar
	for(int i = 1; i < size; i++){
		
		int dif = util[i-1] - util[i];
		if (dif > 0){
			float val = (dif*100.0)/util[i-1];
			
			cout << i+2008 << " deficit del -> " << val << "%" << endl;
		}
		else{
			cout << i+2008 <<  " No hubo deficit " << endl;
		}
		
	}
	
}

int main(){
	//cout << "1. Diferencia - media -> ultimos dos annos / primeros dos annos" << endl << difMedia() <<endl; 
	//cout << "2. Diferencia -> anno con mayor utilidad / anno con menor utilidad" << endl << difMayMenUti() <<endl; 
	//cout << "3. Mediana" << endl << mediana() <<endl; 
	//cout << "4. Diferencia -> Media / Mediana" << endl << difMediaMediana() <<endl; 
	cout << "5. Porcentaje por valor" << endl <<endl; porApo();
	//cout << "6. Deficit del 2017 con respecto al 2016" << endl << deficit20172016() <<endl; 
	//cout << "7. Porcentaje deficit por año" << endl <<endl; porDef();
	
}








