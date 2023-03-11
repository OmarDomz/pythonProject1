import random
from collections import defaultdict

lista = []
contador = defaultdict(int)

for j in range(500000):
    tupla = tuple(random.sample(range(0, 46), 6))
    lista.append(tupla)
    contador[tupla] += 1

tuplas_repetidas = {k: v for k, v in contador.items() if v > 1}
for tupla, cantidad in tuplas_repetidas.items():
    print("La tupla", tupla, "se repite", cantidad, "veces.")

numeros_repetidos = defaultdict(int)
for tupla, cantidad in tuplas_repetidas.items():
    for numero in tupla:
        numeros_repetidos[numero] += cantidad

numeros_repetidos_ordenados = sorted(numeros_repetidos.items(), key=lambda x: x[1], reverse=True)
for numero, cantidad in numeros_repetidos_ordenados:
    print("El número", numero, "se repite", cantidad, "veces.")
#print("Las tuplas que lo contienen son: ", [tupla for tupla in tuplas_repetidas if numero in tupla])
