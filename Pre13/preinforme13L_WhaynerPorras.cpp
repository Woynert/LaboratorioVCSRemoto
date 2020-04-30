#include <iostream>
#include <bits/stdc++.h>
#include <math.h> //raiz cuadrada
#include <string>
//#include <vector>
#include <map> //diccionario
#include <sstream>

using namespace std;

typedef std::map<string, string> dict;


int main(){

	//Credenciales
	string cred[3][2] = {
		{"Woynert", "8008"},
		{"Dayana" , "oct18"},
		{"Kenett" , "superZzz"}
	};

	//Contenidos
	dict m;
  m["Woynert"] = "Bill.pdf|Id.pdf|Sonic.exe";
  m["Dayana"] = "photo1.jpg|photo2.jpg|photo3.jpg|winterMovie.mp4";
  m["Kenett"] = "sporeFullOneLink.rar|Crack.rar|Readme.txt";

  bool succ = false;
  //Comprobar match
  while(!succ){

		//Ingresar credenciales
    string user, pass;
    cout << "\nSign in\nUser: ";
    cin >> user;
    cout << "Password: ";
    cin >> pass;

    for (int i = 0; i <= 3; i++){
    	if ((user == cred[i][0]) && (pass == cred[i][1])){

		   //Mostrar Archivos
			cout << "\nArchivos:\n";
			stringstream s_stream(m[user]); //convertir de string a stringstream
		   	while(s_stream.good()) {
					string substr;
					getline(s_stream, substr, '|'); //obtener string delimitado por |
					cout << " -> " << substr << "\n"; //imprimir
		   	}
		   	succ = true;
		   	break;
			}
		}
		if (!succ){
			cout << "\nError. Try again:\n";
		}
	}


	/*/Breve ejemplo
	typedef std::map<int, string> dictt;
	dictt num;
	num[1] = "Uno";
	num[2] = "Dos";
	num[3] = "Tres";
	num[4] = "Cuatro";
	num[5] = "Cinco";
	num[6] = "Seis";
	num[7] = "Siete";
	num[8] = "Ocho";
	num[9] = "Nueve";
	num[10] = "Diez";

	int NUMB = 0;
	cout << "\nIngrese el numero:\n -> ";
	cin >> NUMB;
	cout << "\nSu numero es " << num[NUMB];*/

	return 0;
}
