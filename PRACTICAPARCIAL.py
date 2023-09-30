# Inicializar las variables
velocidad_maxima = 0 # La velocidad máxima registrada
velocidad_minima = 1000 # La velocidad mínima registrada
velocidad_total = 0 # La suma de las velocidades de todos los ciclistas
contador_30 = 0 # El número de ciclistas que superaron los 30 km/h en al menos una etapa
contador_25 = 0 # El número de ciclistas que mantuvieron más de 25 km/h en todas las etapas
velocidad_etapa_rapida = 0 # La velocidad promedio de la etapa más rápida
velocidad_etapa_lenta = 1000 # La velocidad promedio de la etapa más lenta

# Iterar sobre los 10 ciclistas
for i in range(10):
    # Pedir al usuario la velocidad promedio de cada etapa del ciclista i
    print(f"Ingrese la velocidad promedio del ciclista {i+1} en el tramo medio de cada vuelta (en km/h):")
    velocidad_tramo_medio = float(input())
    print(f"Ingrese la velocidad promedio del ciclista {i+1} en el final de cada vuelta (en km/h):")
    velocidad_final = float(input())

    # Calcular la velocidad promedio del ciclista i
    velocidad_ciclista = (velocidad_tramo_medio + velocidad_final) / 2

    # Actualizar la velocidad máxima y mínima si corresponde
    if velocidad_ciclista > velocidad_maxima:
        velocidad_maxima = velocidad_ciclista
    if velocidad_ciclista < velocidad_minima:
        velocidad_minima = velocidad_ciclista

    # Actualizar la suma de las velocidades de todos los ciclistas
    velocidad_total += velocidad_ciclista

    # Actualizar el contador de ciclistas que superaron los 30 km/h en al menos una etapa si corresponde
    if velocidad_tramo_medio > 30 or velocidad_final > 30:
        contador_30 += 1

    # Actualizar el contador de ciclistas que mantuvieron más de 25 km/h en todas las etapas si corresponde
    if velocidad_tramo_medio > 25 and velocidad_final > 25:
        contador_25 += 1

    # Actualizar la velocidad promedio de la etapa más rápida y más lenta si corresponde
    if velocidad_tramo_medio > velocidad_etapa_rapida:
        velocidad_etapa_rapida = velocidad_tramo_medio
    if velocidad_tramo_medio < velocidad_etapa_lenta:
        velocidad_etapa_lenta = velocidad_tramo_medio
    if velocidad_final > velocidad_etapa_rapida:
        velocidad_etapa_rapida = velocidad_final
    if velocidad_final < velocidad_etapa_lenta:
        velocidad_etapa_lenta = velocidad_final

# Calcular la velocidad promedio general de todos los ciclistas al final de la carrera
velocidad_promedio = velocidad_total / 10

# Mostrar los resultados requeridos
print(f"La velocidad promedio más alta registrada al finalizar el evento fue {velocidad_maxima} km/h.")
print(f"La velocidad promedio más baja registrada al finalizar el evento fue {velocidad_minima} km/h.")
print(f"La velocidad promedio general de todos los ciclistas al final de la carrera fue {velocidad_promedio} km/h.")
print(f"{contador_30} ciclistas tuvieron una velocidad promedio superior a 30 km/h en al menos una etapa de la carrera.")
print(f"{contador_25} ciclistas mantuvieron una velocidad promedio superior a 25 km/h en todas las etapas de la carrera.")
print(f"La velocidad promedio de la etapa más rápida en la carrera fue {velocidad_etapa_rapida} km/h.")
print(f"La velocidad promedio de la etapa más lenta en la carrera fue {velocidad_etapa_lenta} km/h.")
