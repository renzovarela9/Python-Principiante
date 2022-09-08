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

#Limpiar/Inicializar Variables

#Entrada
competidores = 0
nombre = ""
tiempo_carrera= 0.0
tiempo_record = 0.0

#Salida
ganador = ""
promedio = 0.0

#Asignar Valores a las Variables
#Validación:
while (competidores <= 0):
    competidores = int(input("Bienvenido a la finalisima ¿Cuantos competidores son?: "))
    if (competidores <= 0):
        print("Error - no ha ingresado un valor correcto")

for competidores in range (1, competidores +1, 1):
    nombre = str(input("¿Cual es tu nombre?: "))
    tiempo_carrera = float(input("¿En cuanto tiempo finaliso la carrera?: "))
    print("Competidor n°", competidores, nombre,"tu recorrido completo en", tiempo_carrera)
   