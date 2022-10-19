#Menores y promedio: Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:
#Determinar el menor de los numeros generados en forma aleatoria.
#Calcular el valor promedio de los números menores a 10.000.

#Importamos la libreria random para generar números aleatorios
from random import randint

#Declarar Variables
numeros = int()
acumulador = int()
min = int()
promedio = float()

#Limpiar/Inicializar Variables
numeros = 0
acumulador = 0
min = 999999
promedio = 0.0

#Asignar Valores a las Variables
for i in range (0, 5001, 1): #Generamos 5000 numeros 
    numeros = randint(0, 100000) #Entre 0 y 100.000 me va a retornar

    if numeros < 10000:  #Usamos un if para saber cual es menor de todos los numeros generados
        acumulador = numeros + acumulador #Creamos un acumulador para luego dividir por 1000
        promedio = acumulador / 5000
        if numeros < min:  #Usamos un if para saber cual es menor de todos los numeros generados
            min = numeros
    
print("El menor de 5000 números generado entre 0 y 100000 es", min)
print("El promedio de 5000 números generado entre 0 y 100000 es de", promedio)

#P R U E B A  D E  E S C R I T O R I O 
#|Entrada                |Salida                                                                                           |
#|-----------            |El menor de 5000 números generado entre 0 y 100000 es 28
#|                       |El promedio de 5000 números generado entre 0 y 100000 es de 466.004
