# Definir la matriz
matriz = [
    [3, 4, 7],
    [20, 5, 8],
    [11, 2, 9]
]

# Valor a buscar
valor_a_buscar = 7

# Indentificar si se encontró el valor
encontrado = False

# Sobre la matriz buscar el valor
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == valor_a_buscar:
            encontrado = True
            posicion = (i, j)
            break

# Resultado mostrar
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró la matriz.")
