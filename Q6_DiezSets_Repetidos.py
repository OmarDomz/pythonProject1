import random

sets_generados = []
repetidos = 0

while repetidos < 10:
    nuevo_set = set(random.sample(range(0, 47), 6))
    if nuevo_set in sets_generados:
        orden_repetido = sets_generados.index(nuevo_set)
        print(f"El conjunto repetido es {nuevo_set} y se generó en el orden {orden_repetido}")
        repetidos += 1
    else:
        sets_generados.append(nuevo_set)
