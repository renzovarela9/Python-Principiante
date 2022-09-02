#Escribir un programa que pida dos números 
# y muestre como resultado su división, cociente y resto.

#División con resto. Plantear un algoritmo que permita informar, para dos valores a y b 
#el resultado de la división a/b y el resto de esa división.

#Declarar Variables
a = float()
b = float()
resultado = float()

#Inicializar Variables
a = 0.0
b = 0.0
resultado = 0.0

#Asignar Valores a las Variables
a = float(input("Ingrese el primer valor dividendo para dividir: "))
b = float(input("Ingrese el segundo valor divisor para dividir: "))

resultado = a/b
print("El resultado de la division es: ", resultado)

print("El Cociente y Resto de la division es: ", divmod(a,b)) #usamos la funcion divmod para sacar el cociente y el resto

#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida                |
#| ---     | ---                   |
#|17 / 5   | 3.4, ,3.0, 2.0        |