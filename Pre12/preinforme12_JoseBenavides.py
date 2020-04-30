
Lista = [110.06,107.89,108.45,108.49,109.03,110.11,109.87,
         119.38,119.35,116.34,117.73,120.01,118.19,119.53,
         117.09,118.03,118.65,117.47,117.49,109.65,114.44,
         110.51,107.38,109.26,106.188,109.36,106.61,105.16,
         110.11,105.48,108.37,107.59,108.91,108.35,109.57,
         122.41,122.15,124.52,123.35,125.76,121.08,112.29,
         105.42,110.67,107.73,105.76,107.85]
print (len(lista))
lista.sort()
print (lista)
#diferencia entre el mayor y el menor
diferencia = lista[0]-lista[1-]
print (diferencia)

Suma=0
for presion in lista.
    suma += presion

media = suma/len(lista)
print (media)

meridiana= (lista)[25]+lista[26])/2
print (mediana)

# Comparacion = ***La media es mayor debido a que los valores se encuentran mas concentrados a la izquierda

#***Los cambios de las presiones promedio de cada semana pueden darse debido a dos factores importantes para esto
#como lo son la presion y la temperatura que puede cambiar dependiendo del tanteo con la que esta la autoclave
#ya que la calibracion puede variar dependiendo del tiempo, esta tambien influye  en el numero de minutos que puede
#llegar a durar mas o menos de 15 a 20 minutos

temperatura = [(element*510)/(177.16*8.314472)]for element in lista]
print(temperatura)

suma = 0
for i in temperatura:
    suma += i
media = suma/len(temperatura)
print(media)

sumatoria = 0
for h in range (len(temperatura)):
    sumatoria += (temperatura[h]-media)**2

des = (sumatoria/(len(temperatura)-1))**(1/2)
print(des)