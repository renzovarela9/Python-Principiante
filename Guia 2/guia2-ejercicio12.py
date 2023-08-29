#Números pares e impares:
#Se pide desarrollar un programa que permita leer una serie de números.
#La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. 
#Los requerimientos funcionales del programa son: 
#La sumatoria de solo los números que estén comprendidos entre 50 y 100. 
#Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. 
#Informar si en la carga de números se ingreso al menos un número 0.
#Informar si la serie contiene solo números pares e impares alternados.

#Declarar Variables
numero = int()
resto = int()

#Inicializar Variables
numero = 0
resto = 0
#Asignar Valores a las Variables
numero = input("Ingrese un numero:")
resto = numero%2

if (numero == 0): 
    print("es PAR")
else:
    print("es IMPAR")
