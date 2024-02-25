# Matriz
matriz = [
    [7, 4, 9],
    [2, 10, 3],
    [8, 11, 7]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila que a ordenar (en este caso la segunda fila, índice 1)
fila_a_ordenar = 1

# Aplicar Bubble Sort para ordenar la fila indicada
for i in range(len(matriz[fila_a_ordenar])):
    for j in range(len(matriz[fila_a_ordenar]) - 1):
        if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
            # Intercambiar los elementos si están en el orden incorrecto
            matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]


# Mostrar matriz con la fila ordenada
print("Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)




