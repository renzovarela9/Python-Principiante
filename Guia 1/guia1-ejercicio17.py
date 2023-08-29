#Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. 
#Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. 
#El programa deberá verificar si todos los cuadros son anteriores al siglo XX 
#(El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
#Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.

#Analisis
#Entrada          Proceso                                           Salida 
#                 if (cuadro_uno >2013 and cuadro_uno <2023):       antiguedad_10
#                      antiguedad_10 = antiguedad_10 +1             antiguedad
#                 if(cuadro_uno >= 1901 and cuadro_uno <=2000):
#                      antiguedad = antiguedad +1
#                 if (cuadro_uno == 0):
#                      print("Renovar Stock")
#cuadro_uno      
#cuadro_dos
#cuadro_tres 

#Declarar variables
cuadro_uno = int()    
cuadro_dos = int()
cuadro_tres = int()
antiguedad = int()
antiguedad_10 = int()

#Definir variables
cuadro_uno = 0    
cuadro_dos = 0
cuadro_tres = 0
antiguedad = 0
antiguedad_10 = 0

#Programa Principal

cuadro_uno = int(input("Ingrese el año del primer cuadro que fue creado: "))

if (cuadro_uno >2013 and cuadro_uno <2023):
    antiguedad_10 = antiguedad_10 +1
if(cuadro_uno >= 1901 and cuadro_uno <=2000):
    antiguedad = antiguedad +1
if (cuadro_uno == 0):
    print("Renovar Stock")

cuadro_dos= int(input("Ingrese el año del segundo cuadro que fue creado: "))

if (cuadro_dos>2013 and cuadro_dos<2023):
    antiguedad_10 = antiguedad_10 +1
if(cuadro_dos>= 1901 and cuadro_dos<=2000):
    antiguedad = antiguedad +1
if (cuadro_dos== 0):
    print("Renovar Stock")

cuadro_tres= int(input("Ingrese el año del tercer cuadro que fue creado: "))

if (cuadro_tres>2013 and cuadro_tres<2023):
    antiguedad_10 = antiguedad_10 +1
if(cuadro_tres>= 1901 and cuadro_tres<=2000):
    antiguedad = antiguedad +1
if (cuadro_tres== 0):
    print("Renovar Stock")


print("Cuadros con antiguedad menos de 10 años hay: ", antiguedad_10)
print("Cuadros con antiguedad del siglo XX hay: ", antiguedad)



#P R U E B A  D E  E S C R I T O R I O 
#| Entrada         | Salida                                             |
#| ---             | ---                                                |
#|2015, 1988, 2002 | Cuadros con antiguedad menos de 10 años hay:  1    |
#|                 | Cuadros con antiguedad del siglo XX hay:  1        |