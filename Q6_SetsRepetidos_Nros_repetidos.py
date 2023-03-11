import random
from collections import Counter

sets_generados = []
repetidos = []
numeros_repetidos = []

while len(repetidos) < 10:
    nuevo_set = set(random.sample(range(0, 47), 6))
    if nuevo_set in sets_generados:
        repetidos.append(nuevo_set)
    else:
        sets_generados.append(nuevo_set)

for num in range(0, 47):
    freq = Counter([n for s in repetidos for n in s])[num]
    if freq > 0:
        numeros_repetidos.append((num, freq))

print("Números que se repiten y su frecuencia:")
for num, freq in numeros_repetidos:
    print(f"{num}: {freq} veces")
