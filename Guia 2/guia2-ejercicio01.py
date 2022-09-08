#Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). 
# Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
#a) Determinar y mostrar el nombre del ganador de la carrera.
#b) Ingresar por teclado el tiempo record registrado para dicha carrera. 
#Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
#c) Calcular y mostrar el tiempo promedio entre todos los ciclistas


#Declarar Variables

#Entrada
competidores = int()
nombre = str()
tiempo_carrera= float() #Tiempo en realizar la carrera
tiempo_record = float() #Tiempo estimado


#Salida
ganador = str()
promedio = float()
minimo = float()

#Limpiar/Inicializar Variables

#Entrada
competidores = 0
nombre = ""
tiempo_carrera= 0.0
tiempo_record = 0.0


#Salida
ganador = ""
promedio = 0.0
minimo = 999.9

#Asignar Valores a las Variables
#Validación:
while (competidores <= 0):
    competidores = int(input("Bienvenido a la finalisima ¿Cuantos competidores son?: "))
    tiempo_record = float(input("Ingrese el tiempo record estimado: "))
    if (competidores <= 0):
        print("Error - no ha ingresado un valor correcto")

#Usamos el bucle for para ejecutar la cantidad de competidores
for competidores in range (1, competidores +1, 1):
    tiempo_carrera= 0.0 #Limpiamos la variable
    nombre = str(input("¿Cual es tu nombre?: "))
    tiempo_carrera = float(input("¿En cuanto tiempo finalizo la carrera?: "))
    print("Competidor n°", competidores, nombre,"completaste la carrera en: ", tiempo_carrera)
    print("") #Dejamos un espacio para mantener todo mas claro y oredenado


    promedio = promedio + tiempo_carrera #Acumulamos la variable tiempo_carrera para luego sacar el promedio 


    #Usamos esta condicional para guardar el valor minimo del recorrido completo en menor tiempo
    if tiempo_carrera < minimo:
        minimo = tiempo_carrera
        ganador = nombre
    

promedio = promedio / competidores #Divido la variable acumulada del tiempo entre la cantidad de competidores

print("El ganador de esta competición es: ", (ganador.upper()))
print("Ha realizado la carrera en: ", minimo)
print("El promedio entre todo los ciclistas es de: ", promedio)


#                               P R U E B A  D E  E S C R I T O R I O 
#| Entrada                                                    | Salida                                             |
#| ---                                                        | ---                                                |
#|Bienvenido a la finalisima ¿Cuantos competidores son?: 3    |Competidor n° 1 Renzo completaste la carrera en: 8  |
#|Ingrese el tiempo record estimado: 10                       |Competidor n° 1 Ariel completaste la carrera en: 6  |
#|                                                            |Competidor n° 1 Varela completaste la carrera en: 7 |
#|¿Cual es tu nombre?:Renzo                                   |El ganador de esta competición es:  ARIEL           |
#|En cuanto tiempo finalizo la carrera?: 8                    |Ha realizado la carrera en:  6.0                    |
#|                                                            |El promedio entre todo los ciclistas es de:  7.0    |
#|¿Cual es tu nombre?:Ariel                                   |                                                    |
#|En cuanto tiempo finalizo la carrera?: 6                    |                                                    |
#|                                                            |                                                    |
#|¿Cual es tu nombre?:Varela                                  |                                                    |
#|En cuanto tiempo finalizo la carrera?: 7                    |                                                    |

