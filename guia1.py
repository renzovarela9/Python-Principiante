#Ejercicio 1
#Desarrolle un programa que pase un peso de kilogramo a libras 
# teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

#Declaración e inicializacón de Variables
kilogramo = 0.0
libras = 2.2
usuario = 0.0

#Hago que el usuario ingrese el valor a pasar
usuario = float(input("Ingrese el valor para pasar de Kilo gramos a Libras: "))

#igualo las variables para que se realice la conversion
kilogramo = usuario
kilogramo = kilogramo * libras #Multpiplico la cantidad de Kg ingresada por 2.2 libras

print("Has pasado " + str(usuario) + " Kilogramo que equivale a " + str(kilogramo) + " Libras")

#P R U E B A  D E  E S C R I T O R I O 
E N