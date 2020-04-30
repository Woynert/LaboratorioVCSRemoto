import numpy as np

#Credenciales
cred = np.array([["Woynert", "8008"],
                 ["Dayana" , "oct18"],
                 ["Kenett" , "superZzz"]])

#Contenidos
archivos = {"Woynert":["Bill.pdf", "Id.pdf", "Sonic.exe"], 
            "Dayana": ["photo1.jpg", "photo2.jpg", "photo3.jpg", "winterMovie.mp4"], 
            "Kenett": ["sporeFullOneLink.rar", "Crack.rar", "Readme.txt"]}

#Ingresar credenciales
user = input("Credenciales\nUsuario:\n    ")
pas = input("Contraseña:\n    ")


#Mostrar contenido
for i in range(3):
    if (user == cred[i, 0] and pas == cred[i, 1]):
        print("\nSus archivos son:")
        
        txt = ""
        for element in archivos[user]:
            txt += " +  " + element + "\n"
        print(txt)

