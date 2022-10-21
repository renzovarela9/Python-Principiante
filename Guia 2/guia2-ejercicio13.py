#Desarrollar un programa que permita procesar los datos del último censo de un apequeña población.
#Por cada habitantes e ingresa:sexo(M/F)y edad. La carga de datos analiza al ingresar cualquier otro valor para sexo.
#El programa debe informar:Aqué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)
#Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.

#Declarar Variables
mujer = int()
hombre = int ()
edad = int()
edadM = int()
edadF = int()
contador = int()
habitantes = int()
porcentajeM = float()
porcentajeF = float()
opcion = str()

#Limpiar/Inicializar Variables
mujer = 0
hombre = 0
edad = 0
edadM = 0
edadF = 0
contador = 0
habitantes = 0
porcentajeM = 0.0
porcentajeF = 0.0
opcion = ""

#Asignar Valores a las Variables
print("¿Como esta? este programa ha sido codificado para llevar a cabo el censo de su población")
habitantes = int(input("Ingrese la cantidad de habitantes que va a registrar: "))

while contador < habitantes:
    print("Ingrese su sexo: 'M/F' M(Masculino), F(Femenino).")
    opcion = str(input())

    #Validacion
    while opcion != "M" and opcion != "F":
        if opcion != "M" and opcion != "F":
            print("Error-No ingreso el valor correcto")
            opcion = str(input())


    if opcion == "M":
        hombre = hombre +1 #Usamos este contador para saber cuantosd hombres hay

        print("Ingrese la edad que tiene: ")
        edad = int(input())
        
        if edad >= 80:
            edadM = edadM +1 #Usamos este contador para saber cuantos varones mayor a 80 años hay

    if opcion == "F":
        mujer = mujer +1 #Usamos este contador para averiguar cuantas mujeres hay

        print("Ingrese la edad que tiene: ")
        edad = int(input())

        if edad >=4 and edad <=18:
            edadF = edadF +1 #Usamos este contador para saber cuantas mujeres con edad escolar hay

    #Sacamos el porcentaje multiplicando la cantidad de hombres/mujeres por 100 y luego dividimos por la cantidad de habitantes en general 
    porcentajeM = (hombre *100)/ habitantes
    porcentajeF = (mujer *100)/ habitantes

    contador = contador +1 #Este contador es para ponerle un limite al bucle while 


#Cantidad de habitantes
if porcentajeM > porcentajeF:
    print("La mayor cantidad de habitantes corresponde a los varones con el %",porcentajeM,"Y las mujeres con el %",porcentajeF)
else:
    if porcentajeF > porcentajeM:
        print("La mayor cantidad de habitantes corresponde a los mujeres con el %",porcentajeF,"Y los varones con el %",porcentajeM)
    else:
        if porcentajeM == porcentajeF:
             print("La cantidad de habitantes corresponde a ambos por igual, mujeres con el %",porcentajeF,"Y los varones con el %",porcentajeM)

#Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.      
print("La cantidad de mujeres con edad escolar son de: ", edadF)
print("La cantidad de varones que supera la edad de 80 años son de: ", edadM)



# P R U E B A  D E  E S C R I T O R I O 

#|Entrada                |Salida                                                                                                    |
#|                       |¿Como esta? este programa ha sido codificado para llevar a cabo el censo de su población                  |                  
#|habitantes: 2          |Ingrese la cantidad de habitantes que va a registrar:                                                     |                                                                           
#|opcion: M              |Ingrese su sexo: 'M/F' M(Masculino), F(Femenino).                                                         |
#|edad: 89               |Ingrese la edad que tiene:                                                                                |                                      
#|opcion: F              |Ingrese su sexo: 'M/F' M(Masculino), F(Femenino).                                                         |  
#|edad: 12               |Ingrese la edad que tiene:                                                                                |
#|                       |                                                                                                          |                                             
#|                       |La cantidad de habitantes corresponde a ambos por igual, mujeres con el % 50.0 Y los varones con el % 50.0|
#|                       |La cantidad de mujeres con edad escolar son de:  1                                                        |
#|                       |La cantidad de varones que supera la edad de 80 años son de:  1                                           |                                                                                                            

