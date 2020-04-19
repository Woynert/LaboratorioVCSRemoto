import numpy as np

def generador(_min, _max):
    return(np.random.randint(_min, _max, size = 48).reshape(4, 12))

def imprimir(arr):
    
    #indicadores
    citys = np.array(["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"])
    print("Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic\n")
    
    #datos
    for i in range(0, 4):
        txt = ""
        for j in range(0, 12):
            
            txt += str(arr[i,j])
            if (arr[i,j] >= 100):
                txt += "   "
            else:
                txt += "    "
        print(txt + citys[i])
    print("\n")
    
#Crear valores
ingresos = generador(100, 180)
egresos = generador(60, 130)

#Imprimir valores
print("INGRESOS")
imprimir(ingresos)
print("EGRESOS")
imprimir(egresos)