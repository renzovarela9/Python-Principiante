#Escribir un programa que pregunte un nombre de usuario,
#y que después muestre por pantalla si su cantidad de letras es par o impar.

#Declarar Variables
usuario = str()

#Inicializar Variables
usuario = input("Ingrese su nombre: ")

#Asignar Valores a las Variables
if  len(usuario) % 2 == 0: #La función LEN devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada.
    print("Tu nombre es PAR")
else:
    print("Tu nombre es IMPAR")


#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida |
#| ---     | ---    |
#| camilo  | par    |
#| sol     | impar  |