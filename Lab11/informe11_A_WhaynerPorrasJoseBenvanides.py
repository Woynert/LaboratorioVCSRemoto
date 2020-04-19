import numpy as np

#generar arrays
def generador(_min, _max):
    return(np.random.randint(_min, _max, size = 48).reshape(4, 12))

#imprimir array
def imprimir(arr):
    
    #indicadores
    citys = np.array(["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"])
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
    
#crear valores
ingresos = generador(100, 180)
egresos = generador(60, 130)

#imprimir valores
print("INGRESOS")
imprimir(ingresos)
print("EGRESOS")
imprimir(egresos)
print("GANANCIAS")
imprimir(calculador(ingresos, egresos))
