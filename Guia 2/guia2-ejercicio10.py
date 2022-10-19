#Búsqueda de mayor Realizar un programa que permita buscar el mayor de
#10.000 números aleatorios generados en el rango de[0,100.000].

#Importamos la libreria random para generar números aleatorios
from random import randint

#Declarar Variables
numeros = int()
max = int()

#Limpiar/Inicializar Variables
numeros = 0
max = 0

#Asignar Valores a las Variables
for i in range (0, 10001, 1): #Generamos 10.000 numeros 
    numeros = randint(0, 100000) #Entre 0 y 100.000 me va a retornar

    if numeros > max:  #Usamos un if para saber cual es mayor de todos los numeros generados
        max = numeros
    
print("El mayor de 1000 números generado entre 0 y 100000 es", max)

#P R U E B A  D E  E S C R I T O R I O 
#|Entrada                |Salida                                                                                           |
#|-----------            |El mayor de 1000 números generado entre 0 y 100000 es 99976