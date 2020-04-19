import numpy as np


citys = np.array(["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"])

#generar arrays
def generador(_min, _max):
    return(np.random.randint(_min, _max, size = 48).reshape(4, 12))

#imprimir array
def imprimir(arr):
    
    #indicadores
    print("Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic\n")
    
    #datos
    for i in range(0, 4):
        txt = ""
        for j in range(0, 12):
            
            txt += str(arr[i,j])
            
            #acomodar espacios
            if (arr[i,j] >= 100) or (arr[i,j] <= -10):
                txt += "   "
            elif (arr[i,j] >= 10) or (arr[i,j] >= -10) and (arr[i,j] < 0) :
                txt += "    "
            else:
                txt += "     "
                
        print(txt + citys[i])
    print("\n")
    
#restar arrays
def calculador(arrA, arrB):
    arrR = arrA - arrB
    return arrR
    
#más ganancias
def mejor_ciudad(arr):
    
    mejor = 0; #por defecto
    mejorGan = 0;
    
    for i in range(0, 4):
        gan = 0;
        for j in range(0, 12):
            gan += arr[i, j]
        if gan > mejorGan:
            mejorGan = gan
            mejor = i
    print("La ciudad con mejores ganancias fué:\n", citys[mejor], "\nCon ganancias de:",str(mejorGan)+"M COP\n")
            
#menos ganancias
def peor_ciudad(arr):
    
    peor = 0; 
    peorGan = 10000; #valor imposible
    
    for i in range(0, 4):
        gan = 0;
        for j in range(0, 12):
            gan += arr[i, j]
        if gan < peorGan:
            peorGan = gan
            peor = i
    print("La ciudad con peores ganancias fué:\n", citys[peor], "\nCon ganancias de:",str(peorGan)+"M COP\n")
       
#crear valores
ingresos = generador(100, 180)
egresos = generador(60, 130)

#imprimir valores
#print("INGRESOS")
#imprimir(ingresos)

#print("EGRESOS")
#imprimir(egresos)

print("GANANCIAS")
ganancias = calculador(ingresos, egresos)
imprimir(ganancias)

#mejor/peor ciudad
mejor_ciudad(ganancias)
peor_ciudad(ganancias)