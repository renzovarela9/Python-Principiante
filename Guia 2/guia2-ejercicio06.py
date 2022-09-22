#Mostrar por pantalla el promedio de los números ingresados por teclado. 
#Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

#Declarar Variables
numeros = int()
acumulador = int ()
promedio = float()

#Limpiar/Inicializar Variables
numeros = 1
acumulador = 0
promedio = 0.0


#Asignar Valores a las Variables

print("Mostraremos por pantalla su promedio, a traves de numeros que ingrese por teclado.")
print("Para finalizar el programa ingrese 0. ")


#numeros = int(input())

#Hago un bucle para que entre y evalue condiciones
while (numeros >=0 ):
  if(numeros >0 ):  #De lo contrario pedimos que ingrese otro numero
    numeros = int(input("Ingrese un numero para sacar su promedio: "))
    acumulador = acumulador + numeros #Acumulo la variable numeros para realizar luego el promedio.


  #Evalua si la variable numeros es igual a 0
  if (numeros == 0):
    print("")
    print("Fin del programa")
    print("")
    break;


  promedio +=1 # A la variable  promedio hago que se ejecute las veces que ingrese un numero mayor a 0 para luego sacar el promedio de numeros ingresados



print("la suma de los numeos es de", acumulador)

promedio = acumulador  / promedio #Divido la acumulación de numeros por el promedio que se realizo por un contador
print("El promedio es de ", promedio)


        
# P R U E B A  D E  E S C R I T O R I O 

#|Entrada                |Salida                                                                                           |
#|numeros: 7             |Mostraremos por pantalla su promedio, a traves de numeros que ingrese por teclado.               |     
#|                       |Para finalizar el programa ingrese 0.                                                            |
#|                       |                                                                                                 |
#|numeros: 7             |Ingrese un numero para sacar su promedio: 7                                                      |                                      
#|                       |Ingrese un numero para sacar su promedio: 7                                                      |
#|numeros: 7             |Ingrese un numero para sacar su promedio: 7                                                      |                                             
#|                       |Ingrese un numero para sacar su promedio: 0                                                      |
#|numeros: 0             |                                                                                                 |                                         
#|                       |Fin del programa                                                                                 |  
#|                       |                                                                                                 |
#|                       |la suma de los numeos es de 21                                                                   |
#|                       |El promedio es de  7.0                                                                           |                                                        
