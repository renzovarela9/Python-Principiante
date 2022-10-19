#Promedio de números aleatorios: Realice un programa que permita calcular el promedio
#de 1000 números aleatorios generados en el rango de[0,100000].

#Importamos la libreria random para generar números aleatorios
from random import randint

#Declarar Variables
numeros = int()
acumulador = int ()
promedio = float()

#Limpiar/Inicializar Variables
numeros = 0
acumulador = 0
promedio = 0.0

#Asignar Valores a las Variables
for i in range (0, 1001, 1): #Generamos 1000 numeros 
    numeros = randint(0, 100000) #Entre 0 y 100000 me va a retornar 
    acumulador = numeros + acumulador #Creamos un acumulador para luego dividir por 1000
    promedio = acumulador / 1000
    
print("El promedio de 1000 números generado entre 0 y 100000 es de", promedio)

#P R U E B A  D E  E S C R I T O R I O 
#|Entrada                |Salida                                                                                           |
#|-----------            |El promedio de 1000 números generado entre 0 y 100000 es de 50394.861