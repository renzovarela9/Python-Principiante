#Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, 
#cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.

#Declarar Variables
area = float()
base = float()
altura = float()

#Inicializar Variables
area = 0.0
base= 0.0
altura = 0.0

#Asignar Valores a las Variables
base = float(input("Ingrese el valor de la base: "))
altura = base
area = (base * altura ** 2)/2

print("El área de su triangulo es: ", area)

#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida                |
#| ---     | ---                   |
#|3        | 13.5                  |