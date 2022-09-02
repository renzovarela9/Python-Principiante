#Crear un conversor de dólares a pesos y pesos a dólares, 
#donde se ingrese por teclado el valor del peso actual.

#Declarar Variables
from telnetlib import DO


DOLAR_US = float()
pesoArgento = float()
conversion = float()
opcion = int()

#Inicializar Variables
DOLAR_US = 139.16 
pesoArgento = 0.0
conversion = 0.0
opcion = 0


#Asignar Valores a las Variables

print("Bienvenido al conversor de dinero, 1 DOLAR ESTADOUNIDENCE: $139.16 PESO ARGENTINO ")
print("1. Dolar a Peso Argentino")
print("2. Peso Argentino a Dolar")
opcion = int(input("Eliga una opcion: "))

if (opcion <= 0)or(opcion >=3):
    print("Error- vuelva a ingresar de nuevo")

if opcion == 1:
    pesoArgento = float(input("Ingrese la cantidad de dolares que desea convertir: "))
    conversion = pesoArgento* DOLAR_US
    print("Ha convertido", pesoArgento, " dolares por ", conversion, " Peso Argentino")
else:
    if opcion == 2:
        pesoArgento = float(input("Ingrese la cantidad de pesos que desea convertir: "))
        conversion = ((pesoArgento* DOLAR_US) / DOLAR_US)/DOLAR_US
        print("Ha convertido", pesoArgento, " pesos argentinos por ", conversion, " dolares")



#   P R U E B A  D E  E S C R I T O R I O 
#| Entrada          | Salida                |
#| ---              | ---                   |
#|opcion 2: 87 ARS  |  0.62 US              |

