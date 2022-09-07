#Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido,
#Si se pide en cada mes el 10% del sueldo ganado.

#Declarar Variables
ingreso = int()
mes = int()

#Inicializar Variables
ingreso = 0
mes = 0

#Asignar Valores a las Variables

#Entrada
print("Bienvenido Usuario a su registro de ahorros.")
ingreso = int(input("Ingrese la cantidad que ha ganado en Enero: "))

#Enero
if ingreso > 0:
    mes= ingreso / 10
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Febrero: "))

#Febrero
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Marzo: "))

#Marzo
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Abril: "))

#Abril
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Mayo: "))

#Mayo
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Junio: "))

#Junio
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Julio: "))

#Julio
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Agosto: "))

#Agosto
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Septiembre: "))

#Septiembre
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Octubre: "))

#Ocutubre
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Noviembre: "))

#Noviembre
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

#Limpiamos la variable ingreso para el nuevo ingreso de dinero.
ingreso = 0

#Entrada
ingreso = int(input("Ingrese la cantidad que ha ganado en Diciembre: "))

#Diciembre
if ingreso > 0:
    mes= mes + (ingreso // 10)
else:
    print("¿Usted no ha ganado nada?")

print("De tus ingresos el 10% (fue ahorrado) El monto ahorrado en todo el año es:", mes)





