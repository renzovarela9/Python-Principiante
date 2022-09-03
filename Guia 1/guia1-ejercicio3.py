#Escriba un programa que transforme todas las letras de una palabra en mayúsculas, 
#minúsculas y la primera con minúsculas(capitalización).


#Declarar Variables
cadena = str()

#Inicializar Variables
cadena = ""

#Asignar Valores a las Variables
cadena = input("Ingrese una palabra para convertirla en mayúsculas, minúsculas y la primera con minúsculas: ")

print(cadena.upper()) #Para convertir en mayúscula
print(cadena.lower()) #Para convertir en minúscula
print(cadena.capitalize()) #Para convertir la primer letra en mayúscula
#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida                |
#| ---     | ---                   |
#| renzo   | RENZO, renzo, Renzo   |
