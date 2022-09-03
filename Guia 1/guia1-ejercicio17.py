#Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números.
#Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
#en caso contrario elevar el resultado al cubo.


#Declarar Variables
num1 = int()
num2 = int()
num3 = int()
resultado_suma = int()

#Inicializar Variables
num1 = 0
num2 = 0
num3 = 0
resultado_suma = 0

#Asignar Valores a las Variables
num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa en segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

resultado_suma = num1 + num2 + num3

if resultado_suma >10:
    resultado_suma= resultado_suma//2 #Doble barra para realizar una division sin decimal
    print("El resultado de tu suma dividido 2 es: ", resultado_suma)
else:
    resultado_suma= resultado_suma ** 3
    print("El resultado de tu suma elevado al cubo es: ", resultado_suma)

#   P R U E B A  D E  E S C R I T O R I O 
#| Entrada          | Salida                |
#| ---              | ---                   |
#|>10: 10, 10, 10   |  15                   |
