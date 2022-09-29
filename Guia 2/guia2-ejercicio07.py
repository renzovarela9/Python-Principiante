#7. Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. 
#Por cada función se conoce:cantidad de espectadores y descuento(S/N).
#La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:
#Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento 
#y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron 
#y qué porcentaje representan sobre el total de funciones

#Declarar Variables
espectadores = int()
sidescuento = int ()
descuento = int()
funcion = int()

#Limpiar/Inicializar Variables
espectadores = 0
sidescuento = 0
descuento = 0


#Asignar Valores a las Variables

print("Bienvenido a RECUCINES, ingrese la cantidad de entradas que desea comprar")
print("Para finalizar el programa ingrese 0. ")




espectadores = int(input("Ingrese la cantidad de entradas: "))

#Validación
while espectadores < 0:
    if espectadores < 0:
        print("Error- numero de entradas no validos")
        espectadores = int(input("Ingrese la cantidad de entradas: "))


  
#Elije la pelicula          
print("""1. 101 Dalmatas
2. Toy Story: Live Action
3. Gato con botas 2 
4. Piratas del Caribe: Los ultimos tiempos
5. ¿La vida tiene sentido?
6. Sherk 5
7. Avengers: The Return
8. Titanic 2: Mi querido Jack
9. Batman vs Superman 2
10.No juguemos con fuego
11.Los simpons 2""")
  

print("Seleccione la función que quiere ver:")
funcion = int(input())

#Realizamos operaciones segun la funcion que quiere ver
if funcion == 1:
  print("Usted a comprado ", espectadores, "entradas y le sale")

#Evalua si la variable espectador es igual a 0
if (espectadores == 0):
  print("")
  print("Fin del programa")
  print("")
  


