#Cuadrado de un binomio. Plantear un script directamente en el shell de Python, 
#que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.

#Declarar Variables
a = int()
b = int()
binomio = int()
resultado = int()


#Inicializar Variables
a = 0
b = 0
binomio = 0
resultado = 0

#Asignar Valores a las Variables
a = int(input("Ingrese un valor numerico: "))
b = int(input("Ingrese otro valor numerico: "))
binomio = (a + b)**2
resultado = binomio = a ** 2 + 2 * ((a)*(b)) + b ** 2

print(resultado)


#P R U E B A  D E  E S C R I T O R I O 
#| Entrada | Salida                |
#| ---     | ---                   |
#| 5, 3    | 64                    |