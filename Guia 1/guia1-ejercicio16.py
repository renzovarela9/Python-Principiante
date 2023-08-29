#Jornal de un Operario
#Se necesita desarrollar un programa para el área de recursos humanos 
#de una empresa que permita informar el jornal de un determinado operario. 
#Usted deberá cargar por teclado el código de turno
#que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno)
# y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma pueden trabajar
# en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno 
#el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.


#Anaisis
# Entrada        proceso                                         salida
#codigo_turno    DIURNO = 35.50                                  jornal_correspondiente
#cant_horas      NOCTURNO = 40.60
#                //Dependiendo del codigo de 
#                turno se hace el siguente proceso
#             
#                jornal_correspondiente = cant_horas * DIURNO
#                jornal_correspondiente = cant_horas * NOCTURNO

#Declarar Variables
codigo_turno = int()
cant_horas = float()
DIURNO = float()
NOCTURNO = float()
jornal_correspondiente = float()

#Definir variables
codigo_turno = 0
cant_horas = 0.0
DIURNO = 35.50
NOCTURNO = 40.60
jornal_correspondiente = 0.0

#PROGRAMA PRINCIPAL
codigo_turno = int(input("Igrese el codigo de turno: (1- representa Diurno y 2- representa Nocturno): "))

if codigo_turno == 1:
    cant_horas = float(input("Ingrese la cantidad de horas trabajadas: "))
    jornal_correspondiente = cant_horas * DIURNO
elif codigo_turno == 2:
        cant_horas = float(input("Ingrese la cantidad de horas trabajadas: "))
        jornal_correspondiente = cant_horas * NOCTURNO

print("El salario correspondiente es de: $", jornal_correspondiente)

#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida                |
#| ---     | ---                   |
#|1        | 284.0                 |
#|8        |                       |




