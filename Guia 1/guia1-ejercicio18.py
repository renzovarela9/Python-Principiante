#18. Tarjeta de Bingo Realizar un programa que genere 15 numeros aleatorios 
#enteros en el rango del 1 al 100, que representaria la tarjeta de bingo de una persona. 
#Una vez generado los numeros aleatorios solicitar al usuario que ingrese 3 numeros enteros,
#a partir de alli mostrar los siguientes mensajes: 
#Si el usuario no marco ninguno de los numeros indicarlo diciendo
#“El jugador tiene mala suerte, no marco ninguna casilla”. 
#Caso contrario mostrar “El jugador marco algun numero de la tarjeta”. 


#Analisis
#Entrada           proceso                                                    salida
#num_uno           import random
#num_dos           numeros_aleatorios = random.sample(range(1, 101), 15)
#num_tres          if num_uno == numeros_aleatorios or num_dos == numeros_aleatorios or num_tres == numeros_aleatorios:
#                        print(“El jugador tiene mala suerte, no marco ninguna casilla”)  
#                  else:               
#                      print(“El jugador marco algun numero de la tarjeta”)


import random
#Declarar variables
num_uno = int()    
num_dos = int()
num_tres = int()
numeros_aleatorios = int()

#Definir variables
num_uno = 0    
num_dos = 0
num_tres = 0
numeros_aleatorios = 0

#programa principal

numeros_aleatorios = random.sample(range(1, 101), 15)

print("Bienvenido al bingo virtual, ingrese 3 numeros para ver si has marcado algo en tu tarjeta..")
num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))
num_tres = int(input("Ingrese el tercer numero: "))

if num_uno == numeros_aleatorios or num_dos == numeros_aleatorios or num_tres == numeros_aleatorios:
    print("El jugador marco algun numero de la tarjeta", numeros_aleatorios)
      
else:
    print("El jugador tiene mala suerte, no marco ninguna casilla")              
    
#P R U E B A  D E  E S C R I T O R I O 
#| Entrada  | Salida                                                    |
#| ---      | ---                                                       |
#|17, 3, 81 | "El jugador marco algun numero de la tarjeta"             |