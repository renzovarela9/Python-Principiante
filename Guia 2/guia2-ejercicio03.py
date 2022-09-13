#Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
#a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
#b) Determinar en qué mes recibió el sueldo más bajo del período.
#c) Informar el sueldo promedio del semestre.

#Declarar Variables
i = int()
sueldo = int()
aguinaldo = int()
min = int()
max = int()
sueldomenor = int()
promedio = float() 

#Limpiar/Inicializar Variables
i = 0
sueldo = 0
aguinaldo = 0
min = 0
max = 0
sueldomenor = 0
promedio = 0.0 

#Asignar Valores a las Variables
min = 99999999999 #Queremos que el sueldo sea menor a esto

print("""Bienvenido a 'Red de vendedores'. Aqui recibira informes sobre: 
Aguinaldo, sueldo mas bajo obtenido y promedio del primer semestre""")

#Creamos un bucle que se ejecute 6 veces
for i in range(i+1, 7, 1):
    print("Ingrese el sueldo obtenido en el mes del 5 /",i,"/ 2022: ") #Usamos la variable i para imprimir el mes
    sueldo = int(input())

    promedio = promedio + sueldo #Aqui acumulamos el sueldo para luego dividirlo por la cantidad de meses
    
    if (sueldo > max): #Si sueldo es mayor que 0, entonces remplezamos  variables y sacamos el aguinaldo
        max = sueldo
        aguinaldo = max / 2 #El aguinaldo es la mitad del sueldo mas alto
    
    if (sueldo < min): #Si sueldo es menor que 9999999999 entonces remplazamos variables
        sueldomenor = i #Sueldomenor guarda el mes donde se ingreso el sueldo mas bajo
        min = sueldo #Se guarda el sueldo mas bajo
    
   
promedio = promedio / i #La suma de todos los sueldo dividido los meses trabajados.


print("Se calculo su aguinaldo y es de: $",aguinaldo)
print("En el mes del: 5 /",sueldomenor,"/ 2022: Ha recibido el sueldo mas bajo con $",min)
print("El sueldo promedio del semestre del 5 de Enero hasta 5 de Junio es de: $",promedio)


#                                                    P R U E B A  D E  E S C R I T O R I O 
#|Entrada                                                     |Salida                                                                                           |
#|Sueldo:                                                     |Bienvenido a 'Red de vendedores'. Aqui recibira informes sobre:                                  |     
#|                                                            |Aguinaldo, sueldo mas bajo obtenido y promedio del primer semestre                               |
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 1 / 2022:                                           |
#|1000                                                        |                                                                                                 |
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 2 / 2022:                                           |
#|1000                                                        |                                                                                                 |  
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 3 / 2022:                                           |
#|1000                                                        |                                                                                                 |  
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 4 / 2022:                                           |  
#|900                                                         |                                                                                                 |
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 5 / 2022:                                           |
#|1100                                                        |                                                                                                 |
#|                                                            |Ingrese el sueldo obtenido en el mes del 5 / 6 / 2022:                                           |
#|2000                                                        |                                                                                                 |
#|                                                            |Se calculo su aguinaldo y es de: $ 1000.0                                                        |
#|                                                            |En el mes del: 5 / 4 / 2022: Ha recibido el sueldo mas bajo con $ 900                            |
#|                                                            |El sueldo promedio del semestre del 5 de Enero hasta 5 de Junio es de: $ 1166.6666666666667      |     
