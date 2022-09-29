


caracteres = 0
usuario = ""
i = ""
incrementador = 0
contador = 0
contador2 = 0
max = ""

usuario = input("cual es tu nombre ?")

caracteres = len(usuario)

print(caracteres)

for i in usuario:
    incrementador +=1 #Uso esta variable para compararla con el iterador, asi se en que lugar esta cada letra
    print("iteracion", i, incrementador) 
 
    if i in " ":
        print("el espacio esta la casilla: ", incrementador)
       
        subusuario = usuario[0 : incrementador]
            
        
         
        if len(subusuario) > max:
            subusuario = usuario[0 : incrementador]
            max = subusuario
        
print("la palabra mas larga es: ", max)