#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

#Declaracion de variables
n = int
n1 = int
n2 = int
nth = int
count = int

#Definimos las variables
n = 0
n1 = 0
n2 = 0
nth = 0
count = 0


#Usamos un bucle while  y condicionales para hacer la sucecion de Fibonacci
n = int(input("¿Cuántos términos quieres? "))

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Por favor ingresa un número positivo")
elif n == 1:
   print("Sucesión de Fibonacci hasta",n,":")
   print(n1)
else:
   print("Sucesión de Fibonacci:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#P R U E B A  D E  E S C R I T O R I O 

#| Entrada | Salida                |
#| ---     | ---                   |
#| 3       | 0, 1, 1               |