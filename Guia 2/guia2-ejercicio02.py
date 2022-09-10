#Secuencia de impares. Cargar por teclado dos números,
# e imprimir los números impares que se encuentran comprendidos entre ellos,
# en forma ascendente y descendente.


#Declarar Variables
i = int()

#Limpiar/Inicializar Variables
i = 0

#Asignar Valores a las Variables

#usamos el bucle for para ejecutar 2 veces un impresion en pantalla, comienza en 1 termina en 3 y se ejecuta cada un paso
for i in range(1, 3, 1):
    i = int(input("Ingrese un numero: "))
    i= i-2
    
    #Aca evaluamos si es par o impar a traves de la variable i con el operador de módulo para sacar el resto. 
    if  i % 2 == 0:  
        print("Tu numero es PAR")
        print("") #Espacio en blanco
        print("Ascendente: ")
        for i in range(0, i+4, 2): #La variable i guarda el valor del numero ingresado, luego el bucle empieza en 0, se detiene cuando llega a al numero par ingresado y se ejecuta cada  2 pasos
            print(i)

        print("")
        print("Descendente: ")

        for i in range(i, -2, -2): #La variable i guarda el valor del numero ingresado, luego el bucle empieza en la variable i , se detiene cuando llega a al -2 y se ejecuta cada  -2 pasos para descender
            print(i)

    else:
        
        print("Tu numero es IMPAR")
        print("") #Espacio en blanco
        print("Ascendente: ")
        for i in range(1, i+3, 2): #La variable i guarda el valor del numero ingresado, luego el bucle empieza en 1, se detiene cuando llega a al numero impar ingresado y se ejecuta cada  2 pasos
            print(i)

        print("")
        print("Descendente: ")

        for i in range(i, 0, -2): #La variable i guarda el valor del numero ingresado, luego el bucle empieza en la variable i, se detiene cuando llega a al 0 y se ejecuta cada  -2 pasos para descender
            print(i)

#                          P R U E B A  D E  E S C R I T O R I O 
#| Entrada                               | Salida                                             |
#| ---                                   | ---                                                |
#|Ingrese un numero: 8                   |                                                    |
#|                                       |Tu numero es PAR                                    |
#|                                       |Ascendente:                                         |
#|                                       |0                                                   |
#|                                       |2                                                   |
#|                                       |4                                                   |
#|                                       |6                                                   |
#|                                       |8                                                   |
#|                                       |                                                    |
#|                                       |Descendente:                                        |
#|                                       |8                                                   |  
#|                                       |6                                                   |
#|                                       |4                                                   |
#|                                       |2                                                   |
#|                                       |0                                                   |  
#|                                       |                                                    |
#|Ingrese un numero: 7                   |                                                    |
#|                                       |Ascendente:                                         |  
#|                                       |1                                                   |
#|                                       |3                                                   |
#|                                       |5                                                   | 
#|                                       |7                                                   |  
#|                                       |                                                    |
#|                                       |Descendente:                                        |
#|                                       |7                                                   |
#|                                       |5                                                   |
#|                                       |3                                                   |
#|                                       |1                                                   | 










