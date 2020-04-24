#include <iostream>
#include <bits/stdc++.h>
#include <math.h> //raiz cuadrada

using namespace std;

//Impresor
void showTheContent(list<float> l)
{
	int cont = 1;
    list<float>::iterator it;
	for(it = l.begin(); it != l.end(); it++)
	{
		cout << cont << " | " <<  *it << "\n";
		cont++;
	}
	cout << "\n";
}

//Impresor de listas
void showTheContentList(list<list<float> > l)
{
	int cont = 1;
    list<list<float> >::iterator it;
	for(it = l.begin(); it != l.end(); it++)
	{
		showTheContent(*it);
	}
	cout << "\n";
}

//Calculador de desviacion estandar POBLACION
float desviacionEstandarP(list<float> l){
	
	list<float>::iterator it;
	
	//sacar media
	float acu = 0, media = 0, cont = 0;
    for(it = l.begin(); it != l.end(); it++)
	{
		acu += *it;
		cont++;
	}
	media = acu/cont;
	
	//calcular desviación estandar
	acu = 0;
	for(it = l.begin(); it != l.end(); it++)
	{
		acu += pow((*it - media), 2);
	}
	float desEst = sqrt(acu/cont);
	
	return(desEst);
}

//Calculador de desviacion estandar MUESTRA
float desviacionEstandarM(list<float> l){
	
	list<float>::iterator it;
	
	//sacar media
	float acu = 0, media = 0, cont = 0;
    for(it = l.begin(); it != l.end(); it++)
	{
		acu += *it;
		cont++;
	}
	media = acu/cont;
	
	//calcular desviación estandar
	acu = 0;
	for(it = l.begin(); it != l.end(); it++)
	{
		acu += pow((*it - media), 2);
	}
	float desEst = sqrt(acu/cont -1 );
	
	return(desEst);
}

//Kilo pascal a Atmosferas
float kpaToAtm(float kpa){
	return(kpa * 0.009869);
}

int main()
{
	float arr[52] =
	{
	110.06,
	107.89,
	108.45,
	108.49,
	109.03,
	110.11,
	109.87,
	119.38,
	119.35,
	116.34,
	117.73,
	120.01,
	118.19,
	119.53,
	117.09,
	118.03,
	118.65,
	117.47,
	117.49,
	109.65,
	110.44,
	110.51,
	107.38,
	109.26,
	106.18,
	109.36,
	106.61,
	105.16,
	110.11,
	105.48,
	108.37,
	107.59,
	108.91,
	108.35,
	109.57,
	122.56,
	124.44,
	125.97,
	121.03,
	121.22,
	122.41,
	122.15,
	124.52,
	123.35,
	125.76,
	121.08,
	122.29,
	105.42,
	110.67,
	107.73,
	105.76,
	107.85};	
	
	list<float> list1;
	
	//1. Meter los datos
	for(int i = 0; i < 52; i++){
    	list1.push_back(arr[i]);
    }
    cout << "Lista Presion:\n";
	showTheContent(list1);
    
    
    //2. Diferencia mayor y menor
    float may = 0, men = 200;
    list<float>::iterator it;
	for(it = list1.begin(); it != list1.end(); it++)
	{
		//mayor
		if (*it > may){
			may = *it;
		}
		
		//menor
		else if (*it < men){
			men = *it;
		}
	}
	cout << "La diferencia es: " << may << " - "<< men << " = "<< may-men << "\n\n";
    
    //3. Media vs Mediana
    float acu = 0, mediana = 0, media = 0;
    int cont = 1;
    for(it = list1.begin(); it != list1.end(); it++)
	{
		acu += *it;
		
		//mediana
		if (cont == 26 or cont == 27){
			mediana += *it;
		}
		
		cont++;
	}
	media = acu/52;
	mediana /= 2;
    cout << "Media: " << media << " Mediana: " << mediana << "\n\n";
    
    /*/4. Lista Superiores e Inferiores de la media
    list<float> listSup, listInf;
    for(it = list1.begin(); it != list1.end(); it++)
	{
		if (*it > media){
			listSup.push_back(*it );
		}
		else{
			listInf.push_back(*it );
		}
	}
	//listSup.push_back(listInf);
	cout << "Lista Superior:\n";
	showTheContent(listSup);
	cout << "Lista Inferior:\n";
	showTheContent(listInf);*/
	
	//4. Listas consecutivas Superiores e Inferiores de la media PRESION
	list<list<float> > listPresionCons;
	list<float> listCons;
	int supOrNot = false;
	for(it = list1.begin(); it != list1.end(); it++)
	{
		if (*it > media){
			
			if (supOrNot != 1){
				if (!listCons.empty()){
					listPresionCons.push_back(listCons);
					listCons.clear();	
				}
				supOrNot = 1;
			}
			
			if (supOrNot == 1){
				listCons.push_back(*it );
			}
			
		}
		else if (*it < media){
			if (supOrNot != -1){
				if (!listCons.empty()){
					listPresionCons.push_back(listCons);
					listCons.clear();	
				}
				supOrNot = -1;
			}
			
			if (supOrNot == -1){
				listCons.push_back(*it );
			}
		}
	}
	cout << "Listas Presiones Superiores E Inferiores:\n";
	showTheContentList(listPresionCons);
	
	//6.1. Temperatura promedio semanal
	list<float> listTemp;
	float temp = 0;
	for(it = list1.begin(); it != list1.end(); it++)
	{
		temp = (kpaToAtm(*it) * 510) / (17.16 * 0.08205746);
		
		listTemp.push_back(temp);
	}
	cout << "Lista Temperatura:\n";
	showTheContent(listTemp);
	
	//6.2 Desviacion estandar
	cout << "Desviacion estandar temperatura: " << desviacionEstandarP(listTemp) << "\n\n";
	
	//6.3 Lista Superiores e Inferiores de la media TEMPERATURA
	//sacar media
	acu = 0; media = 0; 
    for(it = listTemp.begin(); it != listTemp.end(); it++)
	{
		acu += *it;
	}
	media = acu/52;
	
	//Listas consecutivas Superiores e Inferiores de la media TEMPERATURA
	list<list<float> > listTempCons;
	listCons.clear(); //list<float> listCons;
	supOrNot = false;
	for(it = listTemp.begin(); it != listTemp.end(); it++)
	{
		if (*it > media){
			
			if (supOrNot != 1){
				if (!listCons.empty()){
					listTempCons.push_back(listCons);
					listCons.clear();	
				}
				supOrNot = 1;
			}
			
			if (supOrNot == 1){
				listCons.push_back(*it );
			}
			
		}
		else if (*it < media){
			if (supOrNot != -1){
				if (!listCons.empty()){
					listTempCons.push_back(listCons);
					listCons.clear();	
				}
				supOrNot = -1;
			}
			
			if (supOrNot == -1){
				listCons.push_back(*it );
			}
		}
	}
	cout << "Listas Temperaturas Superiores E Inferiores:\n";
	showTheContentList(listTempCons);
	
	//6.4 Desviaciones estandar de las listas anteriores
	cont = 1;
	float acumu = 0;
	list<list<float> >::iterator itt;
	for(itt = listTempCons.begin(); itt != listTempCons.end(); itt++)
	{
		cout << "Desviacion estandar de lista " << cont << ": " << desviacionEstandarM(*itt) << "\n\n";
		acumu += desviacionEstandarM(*itt);
		cont++;
	}
	
	//6.5 
	cout << "Desviacion estandar listas | Desviacion estandar anual:\n-> ";
	cout << (acumu)/cont << " | " << desviacionEstandarM(listTemp);
	
	
	/*
	//EJEMPLO BREVE DE LA UTILIZACION DE LISTAS EN C++
	list<float> lista;
	
	//datos
	for(int k = 1; k <= 10; k++){
    	lista.push_back(k);
    }
    
    //sacar promedio
    int acum = 0;
    list<float>::iterator itt;
	for(it = lista.begin(); it != lista.end(); it++)
	{
		acum += *it;
	}
    cout << "\nmedia: " << acum/10 << "\n";
	showTheContent(lista);*/
	
	return 0;	
}


