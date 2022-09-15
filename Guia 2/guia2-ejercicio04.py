#Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, 
#por cada uno de ellos mostrar y generar el numero hexadecimal.

#Importamos la libreria random para generar numeros aleatorios
from random import randint

#Declarar Variables
decimal = int()
hexadecimal = int()

#Limpiar/Inicializar Variables
decimal = 0
hexadecimal = 0

#Asignar Valores a las Variables

decimal = randint(5000, 450000) #usamos randint para generar numeros enteros entre el 5000 y el 450000

print("Numero generado aleatoriamente: ",decimal)#imprimimos los numeros generados
print("")
hexadecimal = hex(decimal) #Realizamos la convercion, con la funcion integrada hex() de pyton

print(type(hexadecimal)) #imprimimos la clase para retornar el valor 
print("Su numero convertido en hexadecimal es: ",hexadecimal) #Mostramos por pantalla la conversion 

#ACLARACIÓN: cuando mostramos por pantalla el numero generado y realizamos la conversion, 0x es la representacion del numero hexadecimal convertido.

#                               P R U E B A  D E  E S C R I T O R I O 
#| Entrada                                            | Salida                                             |
#| ---                                                | ---                                                |
#|decimal: 117493                                     |Numero generado aleatoriamente:  117493             |
#|hexadecimal = decimal                               |<class 'str'>                                       |
#|                                                    |Su numero convertido en hexadecimal es:  0x1caf5    |

