

#PARTE B

respuesta='YES'
partidas_ganados_jugador=0
partidas_ganados_tallador=0
partidas_en_total=0
while respuesta=='YES':
    #Punto 11
        
    Ponderado={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
           '8':8,'9':9,'J':10,'Q':10,'K':10}

    #Punto 12
    
    Simbolos=['C','D','T','P']

    #Punto 13

    def Combinar(Ponderado,Simbolos):
        #Se inicializa el diccionario vacío de nombre 'Baraja'
        Baraja={}
        #Se realiza un ciclo for que va de clave en clave en el diccionario de nombre 'Ponderado'
        for key in Ponderado:
            #Se realiza un ciclo for que va de elemento en elemento en la lista de nombre 'Simbolos'
            for elemento in Simbolos:
                #Se agrega al diccionario vacío la clave junto con el símbolo y se le asigna el valor de la clave 
                Baraja[key+elemento]=Ponderado[key]
                #Se retorna el diccionario de nombre 'Baratija'
        return Baraja

    #Punto 14

    def Revolver(Baraja):
        #Se halla la cantidad de llaves del diccionario y se crea una lista vacía la cual contendrá los valores de la llaves
        long=len(Baraja) 
        valores=[]
        #Se realiza un ciclo for el cual vaya de llave en llave en el diccionario, me tome el valor y me lo lleve a la lista 'valores'
        for key in Baraja:
            valores.append(Baraja[key])
    
        import random
        #Se realiza un una copia de la lista valores
        valores_desordenados=valores.copy()
        #Gracias a la librería random podemos desordenar la lista de valores
        random.shuffle(valores_desordenados,random.random)
    
        #Creamos un diccionario vacío que tendrá mi baraja ya revuelta
        Baraja_final={}
        #Se realiza un ciclo for que va desde 0 hasta la cantidad de llaves de la baraja
        for i in range(0,long):
            #Se realiza un ciclo for que va de llave en llave en el diccionario
            for key in Baraja:
                #Se realiza un condicional el cual me permitirá saber a que llave le pertenece el valor
                if valores_desordenados[i]==Baraja[key]:
                    #Se agrega la llave al diccionario vacío y se le asigna el valor 
                    Baraja_final[key]=valores_desordenados[i]
                    #Se elimina la llave del diccionario inicial (Baraja) esto con el fin de que no se vuelva a repetir
                    del Baraja[key]
                    #Se rompe el ciclo
                    break
        #Se retorna el diccionario de nombre 'Baraja_final'
        return Baraja_final
    
    #Punto 16    

    def Repartir(Baraja_final,cartas):
        #Se halla la cantidad de elementos de la lista de las cartas 
        long_cartas=len(cartas)
        #Se crea una lista vacía que tendrá los valores de las llaves de la baraja
        valores=[]
        #Se realiza un ciclo for el cual vaya de llave en llave en el diccionario, me tome el valor y me lo lleve a la lista 'valores'
        for key in Baraja_final:
            valores.append(Baraja_final[key])
    
        import random
        #Se halla la cantidad de elementos de la lista 'valores'
        long=len(valores)
        #Se crea un diccionario copia 
        Baraja_final_copia=Baraja_final.copy()
        #Se realiza un condicional me permite saber cuantas cartas debo darle al usuario según el enunciado
        if long_cartas==0 or long_cartas==1:
            #Se realiza un ciclo for que va desde 0 hasta 2, dos ya que son la cantidad de cartas que debo darle 
            for i in range(0,2):
                #Se genera el número aleatorio en el rango de 0 hasta la cantidad de elementos de la lista valores menos 1
                numero_aleatorio=random.randint(0,long-1)
                #Se realiza un ciclo for el cual va de llave en llave en la baraja
                for key in Baraja_final_copia:
                    #Se realiza un condicional para mirar a a que llave le pertence el valor en la posición del número aleatorio
                    if valores[numero_aleatorio]==Baraja_final_copia[key]:
                        #Se agrega la llave a la lista del jugador, se elimina de la baraja y se acaba el ciclo
                        cartas.append(key)
                        del Baraja_final_copia[key]
                        break
        else:
            #Se genera el número aleatorio en el rango de 0 hasta la cantidad de elementos de la lista valores menos 1
            numero_aleatorio=random.randint(0,long-1)
            #Se realiza un ciclo for que va de llave en llave en la baraja
            for key in Baraja_final_copia:
                #Se realiza un condicional para mirar a a que llave le pertence el valor en la posición del número aleatorio
                if valores[numero_aleatorio]==Baraja_final_copia[key]:
                    #Se agrega la llave a la lista del jugador, se elimina de la baraja y se acaba el ciclo
                    cartas.append(key)
                    del Baraja_final_copia[key]
                    break
        return cartas,Baraja_final_copia
    
    #Punto 17

    def sumar_cartas(Baraja_final,cartas): 
        long=len(cartas)
        suma=0
        for i in range(0,long):
            for key in Baraja_final:
                if cartas[i]==key:
                    suma+=Baraja_final[key]
        return suma
     
    Baraja=Combinar(Ponderado,Simbolos)
    Baraja_final=Revolver(Baraja)
    
    #Punto 15
    cartas_jugador=[]
    cartas_tallador=[]
    cartas_jugador_final,Baraja_final_copia=Repartir(Baraja_final,cartas_jugador)

    #Punto 18 y 19
    
    #Se le dá información al jugador de la suma de sus cartas
    print("El valor de sus cartas como jugador es",sumar_cartas(Baraja_final,cartas_jugador))
    #Se realiza un condicional en caso de que la suma de las cartas de dé diferente a 21
    if sumar_cartas(Baraja_final,cartas_jugador)!=21:
        #Se le pregunta al usuario si desea otra carta
        respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
        #Se realiza un ciclo for para que cada vez que el usuario digite que 'si' me realice el procedimiento
        while respuesta=='si':
            #Por medio de la función repartir se le da una carta al jugador
            cartas_jugador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_jugador_final)
            #Se calcula la suma de sus cartas y se le muestra al usuario
            suma_jugador=sumar_cartas(Baraja_final,cartas_jugador_final)
            print("El valor de sus cartas como jugador es",suma_jugador)
            #Si la suma es igual a 21 se le informará al usuario y el ciclo se acabará
            if suma_jugador==21:
                print("Usted ya ha completado 21")
                break
            #En caso de que la suma sea mayor a 21 se le informará al usuario que ha perdido debido a que se pasó de 21 y el ciclo llegará a su fin
            elif suma_jugador>21:
                print("Usted ha perdido al pasar de 21")
                break
            #En caso de que ninguna de estas condiciones se cumpla se preguntará al jugador si desea otra carta
            respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
    else:
        #En caso de que la primera condición no se cumpla el usuario habrá ganado automáticamente
        print("Usted ha ganado, felicitaciones!")
    
    #Con las cartas del tallador se hace exactamente el mismo procedimiento que con las cartas del jugador
    cartas_tallador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_tallador)
    print("El valor de sus cartas como tallador es",sumar_cartas(Baraja_final,cartas_tallador))
    if sumar_cartas(Baraja_final,cartas_tallador)!=21:
        respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
        while respuesta=='si':
            cartas_tallador_final,Baraja_final_copia=Repartir(Baraja_final_copia,cartas_tallador_final)
            suma_tallador=sumar_cartas(Baraja_final,cartas_tallador_final)
            print("El valor de sus cartas como tallador es",suma_tallador)
            if suma_tallador==21:
                print("Usted ya ha completado 21")
                break
            elif suma_tallador>21:
                print("Usted ha perdido al pasar de 21")
                break
            respuesta=input("¿Desea otra carta? Si así lo desea escriba 'si' de lo contrario escriba 'no':")
    else:
        print("Usted ha ganado, felicitaciones!")
    
    #Se realizan condicionales los cuales me ayudarán a determinar quien fue el ganador de la partida y dependienedo de quien haya ganado me sumará de a uno al contador
    if sumar_cartas(Baraja_final,cartas_jugador_final)>sumar_cartas(Baraja_final,cartas_tallador_final) and sumar_cartas(Baraja_final,cartas_jugador_final)<=21 or sumar_cartas(Baraja_final,cartas_tallador_final)>21:
        print("El jugador ha ganado en esta partida")
        partidas_ganados_jugador+=1
    elif sumar_cartas(Baraja_final,cartas_tallador_final)>sumar_cartas(Baraja_final,cartas_jugador_final) and sumar_cartas(Baraja_final,cartas_tallador_final)<=21 or sumar_cartas(Baraja_final,cartas_jugador_final)>21 or sumar_cartas(Baraja_final,cartas_tallador_final)==sumar_cartas(Baraja_final,cartas_jugador_final):
        print("El tallador ha ganado en esta partida")
        partidas_ganados_tallador+=1
    #Se suma uno al contador de las partidas y se le pregunta al usuario si desea jugar otra partida
    partidas_en_total+=1
    respuesta=input("¿Desea jugar otra partida nueva? Si así lo desea digite 'YES', de lo contrario digite 'NO':")   

#Punto 20
#Se imprime el resultado final
print("Se jugaron",partidas_en_total,"partidas en total de las que en",partidas_ganados_jugador,"ganó el jugador y en",partidas_ganados_tallador,"ganó el tallador")
