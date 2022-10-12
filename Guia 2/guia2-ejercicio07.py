#7. Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. 
#Por cada función se conoce:cantidad de espectadores y descuento(S/N).
#La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:
#Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento 
#y $75 en los días sin descuento.
#Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones

#Declarar Variables
espectadores = int()
descuento = int()
recaudacionS = int()
recaudacionN = int()
funcionS = int()
funcionN = int()
funcion = int()
funcionGeneral = int()
opcion = str()

#Limpiar/Inicializar Variables
espectadores = 0
descuento = 0
recaudacionS = 0
recaudacionN = 0
funcionS = 0
funcionN = 0
funcion = 0
funcionGeneral = 0
opcion = ""

#Asignar Valores a las Variables
while espectadores >= 0:
  espectadores= int(input("Ingrese la cantidad de espectadores (La carga termina cuando ingrese 0): "))
  #Validación
  while espectadores < 0: #No dejamos que el usuario ingrese numeros negativos
    if espectadores < 0:
        print("Error-Ingreso no valido")
        espectadores= int(input("Ingrese la cantidad de espectadores (La carga termina cuando ingrese 0): "))

  if espectadores > 0:
    opcion = str(input("Ingrese 'Si' con descuento (Vale Martes y Juves) o 'No' sin descuento (Vale Lunes, Miercoles, Viernes y Domigo): "))
    opcion = opcion.lower()
    #Validación
    while opcion != 'si' and opcion != 'no': #No dejamos que el usuario ingrese cualquier cosa
      if opcion != 'si' and opcion != 'no':
        print("Error-El valor que ingreso no corresponde")
        opcion = str(input("Ingrese 'Si' con descuento (Vale Martes y Juves) o 'No' sin descuento (Vale Lunes, Miercoles, Viernes y Domigo): "))
        opcion = opcion.lower()

    if opcion == "si":
      descuento = 50
      recaudacionS = espectadores * descuento #Multiplicamos el precio de la entrada por el descuento
      funcionS = funcionS +1 #Contador para luego sacar el porcentaje
  
    elif opcion == "no":
      descuento = 75
      recaudacionN = espectadores * descuento #Multiplicamos el precio de la entrada por sin el descuento
      funcionN = funcionN +1 #Contador para luego sacar el porcentaje

  #Fin del programa
  if espectadores == 0:
    break;

  funcion = funcion +1 #Contador para luego sacar el porcentaje

funcionGeneral = ((funcionS *100) / funcion) #Usamos regla de 3 simples para el porcentaje

print("Se hizo %",funcionGeneral,"Funciones con descuento")



# P R U E B A  D E  E S C R I T O R I O 

#|Entrada                |Salida                                                                                                          |
#|espectadores: 7        |Ingrese la cantidad de espectadores (La carga termina cuando ingrese 0):                                        |                  
#|opcion: si             |Ingrese 'Si' con descuento (Vale Martes y Juves) o 'No' sin descuento (Vale Lunes, Miercoles, Viernes y Domigo):|                                                                           
#|                       |                                                                                                                |
#|espectadores: 7        |Ingrese la cantidad de espectadores (La carga termina cuando ingrese 0):                                        |                                      
#|opcion: no             |Ingrese 'Si' con descuento (Vale Martes y Juves) o 'No' sin descuento (Vale Lunes, Miercoles, Viernes y Domigo):|  
#|                       |                                                                                                                |
#|espectadores: 7        |Ingrese la cantidad de espectadores (La carga termina cuando ingrese 0):                                        |                                             
#|opcion: no             |Ingrese 'Si' con descuento (Vale Martes y Juves) o 'No' sin descuento (Vale Lunes, Miercoles, Viernes y Domigo):|
#|                       |                                                                                                                |
#|espectadores: 0        |Se hizo % 33.333333333333336 Funciones con descuento                                                            |                                                                                                            
