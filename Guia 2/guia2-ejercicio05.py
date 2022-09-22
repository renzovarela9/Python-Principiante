#Analisis de Texto.
#El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. 
#La frase finaliza con un punto, y las palabras están separadas por espacios únicamente. Se debe mostrar:
#a) Ver el porcentaje de vocales respecto del total de letras de la frase.
#b) La longitud promedio de las palabras.
#c) La longitud de la palabra mas larga del texto.
#d) Cantidad de palabras que comienzan con "ta".

#Declarar Variables
usuario = str()
subusuario = str()
i = str()
incrementador = int()
contador = int()
contador2 = int()
porcentaje = float()
#Inicializar/limpiar Variables
usuario = ""
subusuario = ""
i = "" #Iteracion
incrementador = 0
contador = 0
contador2 = 0
porcentaje = 0.0

#Asignar Valores a las Variables


usuario = input("¿Cual es tu nombre?: ")
usuario = usuario.lower()
usuario = usuario.strip(" ") # Borramos los espacios al inicio y final
for i in usuario:
    #CONTADOR DE VOCALES
    if i in "aeiouáéíóú":
        contador = contador+1
    
    incrementador +=1 #Uso esta variable para compararla con el iterador, asi se en que lugar esta cada letra
    print("iteracion", i, incrementador) 

    #CONTADOR DE ESPACIOS
    if i in " ":
        print("el espacio esta la casilla: ", incrementador)
        contador2 = contador2 +1 
       # subusuario = contador2 - incrementador
        #print("prueba sobre palabra mas larga",subusuario)





print("La cantidad de vocales usadas son: ", contador)

print(usuario)
#PORCENTAJE DE VOCALES   
porcentaje = ( contador * 100)
porcentaje = porcentaje / len(usuario) 
print("El resultado de vocales usadas en la frase es de: ", porcentaje,"%")




print("La cantidad de espacio que hay son: ", contador2)


#subusuario = usuario[0 : 3]
#print(usuario)