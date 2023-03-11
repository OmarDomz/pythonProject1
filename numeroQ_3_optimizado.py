import random
import time

start_time = time.time()
lista = []
indices_repetidos = set()

for j in range(50000):
    tupla = tuple(random.sample(range(0, 46), 6))
    lista.append(tupla)
    for i in range(j):
        if lista[i] == tupla:  # "ya está anteriormente en la lista"
            indices_repetidos.add(i)

tuplas_repetidas = [lista[i] for i in indices_repetidos]
tuplas_repetidas_unicas = set(tuplas_repetidas)
end_time = time.time()
elapsed_time = end_time - start_time
print("Tiempo de ejecución: %s segundos" % (time.time() - start_time))

print("Hay", len(tuplas_repetidas), "tuplas repetidas.")
print("Son:", tuplas_repetidas)
print("Hay", len(tuplas_repetidas_unicas), "tuplas repetidas una o ms veces.")
print("Son:", tuplas_repetidas_unicas)