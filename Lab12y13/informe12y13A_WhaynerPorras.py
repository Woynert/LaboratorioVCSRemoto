# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:02:19 2020

@author: Woynert
"""
import random


cartas =  ["Payne", "Hendrix", "Stone", "Coffey", "Whitaker", "Pope", "Bleach", "Arc", "Fleming", "Hardin", "Robiar", "Mccullough", "Mooney", "Reynolds", "Short", "Stanton", "Deadman", "Stonehammer", "Smith", "Patrick", "Crane", "Cargane", "Powers", "Wade", "Joseph", "Savage", "Houston", "Merritt", "Nuke", "Barnett", "Acosta", "Duke", "Sellers", "Blake", "Schneider", "Stone", "Cannon", "Garrison", "Randall", "Leon", "Buck", "Shannon", "Delaney", "Mckinney", "Dodademocles", "Flowers", "Whitehead", "Kirby", "Park", "Shannon", "Vlad", "Pepin", "Mcguire", "Murray", "Rush", "Aramis", "Fletcher", "Mcfadden", "Deleon", "Luke", "Lindsay", "Payne", "Gerbvo", "Hubbard", "Burnett", "Bryan", "Ratliff", "Carlson", "Parsons", "Deadmeat", "Crimson", "Wilson", "Terry", "Hancock", "Hightower", "Burns", "Austin", "Nightwalker", "Thetis", "Owen", "Tate", "Simmons", "Grant", "Barber", "Talos", "Ashes", "Alston", "Clayton", "Mcbride", "Huffman", "Lightbringer", "Blankenship", "Higgins", "Saint", "Graham", "Hodor", "Ellison", "Roberts", "Odom", "Mann"]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]


#Input -> Lista
def imprimir(lista):
    print("\nTamaño: " + str(len(lista)))
    print("Contenido: " + str(lista))
    
#Revuelve listas
#Input -> Lista, entero / Output -> Lista  
def generador(lista, size):
    
    maxInd = len(lista)
    sortedList = [] #nueva lista reordenada
    
    #no puede ser mayor
    if size <= maxInd:
        
        notUsedList = [] #llena
        
        #Rellenar index
        for i in range(0, maxInd):
            notUsedList.append(i)
        
        #Vaciar index
        while len(sortedList) < size:
            temInd = random.randint(0, len(notUsedList) -1)
            sortedList.append(lista[notUsedList[temInd]])
            notUsedList.pop(temInd)
            
    return(sortedList)
    
#Une y revuelve dos listas
#Input -> Lista / Output -> Lista  
def combinador(lista1, lista2):
    return(generador(lista1 + lista2, len(lista1) + len(lista2)))
    
#Dar una carta
#Input -> Lista / Output -> String
def loteria(lista1, lista2):
    
    #duplicados
    duplicados = [element for element in lista1 if lista1.count(element) > 1]
    
    #tiene mas de una premium
    premiums = [element for element in lista1 if premium.count(element) > 0]
    
    #10%
    pasa = (random.randint(1, 10) == 1)
    
    #Requisitos: Duplicados, menos de 2 cartas premium
    if pasa and (len(duplicados) > 0) and (len(premiums) <= 1):
        premiumCopy = [""]
        premiumCopy = generador(premium, len(premium))
        
        for i in range(0, len(premiumCopy)):
            if (lista1.count(premiumCopy[i]) + lista2.count(premiumCopy[i])) == 0:
                return(premiumCopy[i])
    else:
        return(None)
    
#imprimir(cartas)
#imprimir(premium)

jugador = [""]
jugador = generador(cartas, 10)
#imprimir(jugador)

juego = [""]
juego = combinador(cartas, premium)
#imprimir(juego)

subJuego = juego.copy()

#Crear sobre uno
sobre_uno = generador(subJuego, 5)
    
#Crear sobre dos
sobre_dos = generador(subJuego, 5)
    
#Crear sobre tres
sobre_tres = generador(subJuego, 5)
    
#imprimir(sobre_uno)
#imprimir(sobre_dos)
#imprimir(sobre_tres)

paquete = [""]
paquete = combinador(combinador(sobre_uno, sobre_dos), sobre_tres)
#imprimir(paquete)

newCard = loteria(paquete, jugador)
#print(newCard)

jugador = jugador + paquete
imprimir(jugador)

#Si el jugador tuvo cartas premiums y cuales fueron
premiums = [element for element in jugador if premium.count(element) != 0]
#imprimir(premiums)

#cuantas cartas repetidas tuvo el jugador
Nduplicados = len([element for element in jugador if jugador.count(element) > 1])
print("Numero de cartas duplicadas: ", Nduplicados)

#cantidad de veces que aparece cada carta
cantCartas = []
for i in range(0, len(jugador)):
    if cantCartas.count(jugador[i]) == 0:
        cantCartas.append([jugador[i], jugador.count(jugador[i])])

#imprimir cantidad de veces que aprece una carta
for i in range(0, len(cantCartas)):
    print(cantCartas[i][0], " -> ", cantCartas[i][1])

#cantidad de veces que una carte empieza con una letra
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
lettCartas = []
for i in range(0, len(letters)):
    lettCartas.append([letters[i], len([element for element in jugador if element.lower()[0] == letters[i]])])
    
#imprimir
for i in range(0, len(lettCartas)):
    print(lettCartas[i][0], " -> ", lettCartas[i][1])
    
#carta mas larga y corta
larg = ""
cort = ""
for i in range(0, len(jugador)):
    #Corta
    if len(jugador[i]) < len(cort) or cort == "":
        cort = jugador[i]
    #Larga
    if len(jugador[i]) > len(larg):
        larg = jugador[i]
print("Nombre más largo: ", larg)
print("Nombre más cort: ", cort)


#cuantas cartas terminan con la letra con la que empiezan las premiums obtenidas

#sacar las premiums obtenidas
jugaPre = [element for element in jugador if element in premium]
listCartas = []

#comprobar
if len(jugaPre) > 0:
    for i in range(0, len(juego)):
        for j in range(0, len(jugaPre)):
            if juego[i].lower()[-1] == jugaPre[j].lower()[0]:
                listCartas.append(juego[i])
    print("Premiums:\n", str(jugaPre))
    print("\nNormales:\n", str(listCartas))

else: #no tiene 
    print("No tiene cartas premium")
    
#Cuantas veces aparecen letras consecutivas y cuantas veces
listLetRep = []
let = ""
cant = 1

for i in range(0, len(juego)):
    let = ""
    cant = 1
    for j in range(0, len(juego[i])):
        if let == juego[i][j]:
            cant += 1
        if cant > 1:
            listLetRep.append([juego[i], let, cant])
        cant = 1
        let = juego[i][j]
            
#imprimir
txt = ""
for i in range(0, len(listLetRep)):
    txt += str(listLetRep[i]) + "\n"
print(txt)
        
#cuantas veces hay tantas letras
listLetCant = []
acum = 0
for i in range(0, len(letters)):
    cant = 0
    for j in range(0, len(jugador)):
        cant += jugador[j].count(letters[i])
    acum += cant
    listLetCant.append([letters[i], cant])
    
#imprimir
txt = ""
for i in range(0, len(listLetCant)):
    txt += str(listLetCant[i]) + " : " + str(round(listLetCant[i][1] / acum * 100, 2)) + " %\n"
print(txt)       

