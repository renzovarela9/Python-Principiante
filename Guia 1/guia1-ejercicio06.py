#Últimos dígitos ¿Cómo usaría el operador resto (%)
#para obtener el valor del último dígito de un número entero?
#¿Y cómo obtendría los dos últimos dígitos?
#Desarrolle un programa que cargue un número entero por teclado, 
#y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).

#Declarar Variables
num = int()
digit1 = int()
digit2 = int()

#Inicializar Variables
num = 0
digit1 = 0
digit2 = 0

#Asignar Valores a las Variables
num = int(input("Ingrese un numero para obetener el ultimo digito: "))
num= num % 10 #Hacemos que ingrese un valor para sacar el % 10 y ultimo digito.

print("Su ultimo digito es: ", num)

num = 0 #Limpiamos variables

num = int(input("Ingrese un numero para obetener sus ultimos 2 digitos: "))
num= num % 100 #Hacemos que ingrese un valor para sacar el % 100 y ultimos 2 digitos.


print("Su ultimo digito es:", num)



#                               P R U E B A  D E  E S C R I T O R I O 
#| Entrada                                                    | Salida                         |
#| ---                                                        | ---                            |
#|Ingrese un numero para obetener el ultimo digito:15         |Su ultimo digito es: 5          |
#|Ingrese un numero para obetener sus ultimos 2 digitos: 137  |Sus ultimos 2 digitos son:  37  |

