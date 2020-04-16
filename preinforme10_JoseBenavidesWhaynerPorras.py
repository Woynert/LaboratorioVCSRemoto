import numpy as np 

"""
Integrantes del grupo:
- Whayner Eduardo Porras Rodriguez
- José Santiago Benavides Céspedes
"""

#info
def utilidad():
    utilidad = np.array([27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834])
    return utilidad

#1. Diferencia - media -> últimos dos años / primeros dos años
def ejercicio1(utilidad):
    cant = len(utilidad)
    prom1= (utilidad[cant-1]+utilidad[cant-2])/2
    prom2= (utilidad[0] + utilidad[1])/2
    dif = abs(prom1 - prom2)
    return dif

#2. Diferencia -> año con mayor utilidad / año con menor utilidad
def ejercicio2(utilidad):
    cant = len(utilidad)
    dif = (utilidad[5] - (utilidad[9]))
    return dif

#3. Mediana
def ejercicio3(utilidad):
    orden = np.sort(utilidad)
    mediana = (orden[5]+ orden[6])/2
    return mediana

#4. Diferencia -> Media / Mediana
def ejercicio4(utilidad):
    
    #total
    mediana = (ejercicio3(utilidad))
    med = 0
    cant = len(utilidad)
    for i in range(0,cant):
        med += utilidad[i]
        
    #calculo
    med = med/cant
    prom = med/cant
    print("La diferencia entre la media y la mediana es: " + str(abs(mediana - med)))
    
#5. Porcentaje por valor
def ejercicio5(utilidad):
    
    #obtener total
    acum = 0
    cant = len(utilidad)
    for i in range(0, cant):
        acum += utilidad[i]
        
    #comparar
    porc = 0
    a = 2007
    for i in range(0, cant):
        porc = (utilidad[i]*100)/acum
        a += 1
        print("El porcentaje que aporta el año " + str(a) + " al acumulado es: " + str(porc) + "%")
        
#6. Deficit del 2017 con respecto al 2016
def ejercicio6(utilidad):
    cant = len(utilidad)
    deficit = (utilidad[8] - (utilidad[9]))
    return deficit

#7. Porcentaje deficit por año
def ejercicio7(utilidad):
    
    #calcular
    cant= len(utilidad)
    a = 2007
    for i in range(0, cant-1):
        d = utilidad[i] - utilidad[i+1]
        deficit = (d*100/utilidad[i])
        a += 1
        print(str("El deficit del año " + str(a) + " es " + str(deficit)))
        

utilidad = utilidad()

"""
Para probar las funciones desbloquee la parte que le interesa
"""

#print("La diferencia de la media es: " + str(ejercicio1(utilidad)))
#print("La diferencia del mayor y el menor es: " + str(ejercicio2(utilidad)))
#print("La mediana es " + str(ejercicio3(utilidad)))
#ejercicio4(utilidad)   
#ejercicio5(utilidad)
#print("El decifit del año 2017 en comparación al anterior es: " + str(ejercicio6(utilidad)) + " Millones de COP")
ejercicio7(utilidad)
  

