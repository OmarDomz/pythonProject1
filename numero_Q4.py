import random
from collections import defaultdict

lista = []
contador = defaultdict(int)

for j in range(500000):
    tupla = tuple(random.sample(range(0, 46), 6))
    lista.append(tupla)
    contador[tupla] += 1

tuplas_repetidas = {k: v for k, v in contador.items() if v > 1}
print(tuplas_repetidas)
