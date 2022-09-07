#Crear un conversor de pies y pulgadas a centímetros.


#Declarar Variables
pie = int()
PULGADA = int()
CM = float()
conversionP = float()
conversionC = float()

#Inicializar Variables
pie = 0
PULGADA = 12
CM = 30.48
conversionP = 0.0
conversionC = 0.0

#Asignar Valores a las Variables
print("Bienvenido al conversor de LONGITUD, 1 PIE son 12 PULGADAS = 30.48 CENTIMETROS ")
pie = int(input("Ingrese la cantidad de pies que desea convertir a centímetros: "))

conversionP = pie * PULGADA

conversionC = pie * CM

print("Has convertido ", pie, "Pies, equivalen a ", conversionP, "Pulgadas, y son ", conversionC, "Centimetros")

#   P R U E B A  D E  E S C R I T O R I O 
#| Entrada          | Salida                |
#| ---              | ---                   |
#|10                |  10, 120, 304.8       |
