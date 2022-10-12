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
palabra_ta = str()
incrementador = int()
contador = int()
contador2 = int()
palabralarga = int()
porcentaje = float()

#Inicializar/limpiar Variables
usuario = ""
subusuario = ""
i = "" #Iteracion
incrementador = 0 #Cuenta y la posicion de cada letra
palabra_ta = ""
contador = 0
contador2 = 0
palabralarga = 0
porcentaje = 0.0

#Asignar Valores a las Variables
usuario = input("¿Cual es tu nombre?: ")
usuario = usuario.lower()
usuario = usuario.strip(" ") # Borramos los espacios al inicio y final
for i in usuario:
    #CONTADOR DE VOCALES #RESPUESTA A
    if i in "aeiouáéíóú":
        contador = contador+1
    

print("La cantidad de vocales usadas son: ", contador) #RESPUESTA A

#PORCENTAJE DE VOCALES   #RESPUESTA B
porcentaje = ( contador * 100)
porcentaje = porcentaje / len(usuario) 
print("El resultado de vocales usadas en la frase es de: ", porcentaje,"%")











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
palabra_ta = str()
incrementador = int()
contador = int()
contador2 = int()
palabralarga = int()

porcentaje = float()

#Inicializar/limpiar Variables
usuario = ""
subusuario = ""
i = "" #Iteracion
incrementador = 0 #Cuenta y la posicion de cada letra
palabra_ta = ""
contador = 0
contador2 = 0
palabralarga = 0
porcentaje = 0.0

#Asignar Valores a las Variables

usuario = input("¿Cual es tu nombre?: ")
usuario = usuario.lower()
usuario = usuario.strip(" ") # Borramos los espacios al inicio y final
for i in  range (len(usuario)):
    #CONTADOR DE VOCALES #RESPUESTA A
    #if i in "aeiouáéíóú":
     #   contador = contador+1
    
     #CONTADOR DE ESPACIOS
    if i == " ":
        print("el espacio esta la casilla: ", incrementador)
        contador2 = contador2 +1 
        
    subusuario = usuario[0 : contador2]; 
    usuario = usuario[contador2+1 : usuario.find(".")+1];  
    #PALABRA MAS LARGA    #RESPUESTA C
    if (len(subusuario) > palabralarga):
        palabralarga = len(subusuario)




#palabra_ta = usuario.find("ta")     #RESPUESTA D
#for palabra_ta[0 : 2]  in "ta":
 #   subusuario = palabra_ta 
 #   contador2 = contador2 +1 
     




print("La cantidad de vocales usadas son: ", contador) #RESPUESTA A


#PORCENTAJE DE VOCALES   #RESPUESTA B
#porcentaje = ( contador * 100)
#porcentaje = porcentaje / len(usuario) 
#print("El resultado de vocales usadas en la frase es de: ", porcentaje,"%")

#PALABRA MAS LARGA         #RESPUESTA C
print("La palabra mas larga tiene:", palabralarga," Letras")
#PALABRAS CON TA      #RESPUESTA D
#print("Palabras que empienzan con 'ta' : ",contador2)



