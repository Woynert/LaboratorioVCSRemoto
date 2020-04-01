#Variables

a = float(input("Ingrese el numero a --> "))
b = float(input("Ingrese el numero b --> "))
c = float(input("Ingrese el numero c --> "))

d = (b**2)-4*a*c

if (d > 0):
    x1 = (-b+(d**(1/2)))/(2*a)
    x2 = (-b-(d**(1/2)))/(2*a)
    print("Solución\nx1 = ",x1,"\nx2 = ",x2)
elif (d == 0):
    x1 = (-b)/(2*a)
    print("Solución\nx1 = ",x1)
elif (d < 0):
    print("No existe una solución que esté dentro de los numeros reales")
    

