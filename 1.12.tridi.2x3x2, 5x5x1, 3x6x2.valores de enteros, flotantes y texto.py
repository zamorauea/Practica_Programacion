import numpy as np

# Declaración de variables tridimensionales y asignación de valores de enteros, flotantes y texto
array_2x3x2 = np.array([
    [[1, 2],
     [3, 4],
     [5, 6]],

    [[7, 8],
     [9, 10],
     [11, 12]]
])

array_5x5x1 = np.array([
    [[0.1],
     [0.2],
     [0.3],
     [0.4],
     [0.5]],

    [[1.1],
     [1.2],
     [1.3],
     [1.4],
     [1.5]],

    [[2.1],
     [2.2],
     [2.3],
     [2.4],
     [2.5]],

    [[3.1],
     [3.2],
     [3.3],
     [3.4],
     [3.5]],

    [[4.1],
     [4.2],
     [4.3],
     [4.4],
     [4.5]]
])

array_3x6x2 = np.array([
    [[10, 20],
     [30, 40],
     [50, 60],
     [70, 80],
     [90, 100],
     [110, 120]],

    [[0.5, 0.6],
     [0.7, 0.8],
     [0.9, 1.0],
     [1.1, 1.2],
     [1.3, 1.4],
     [1.5, 1.6]],

    [["texto1", "texto2"],
     ["texto3", "texto4"],
     ["texto5", "texto6"],
     ["texto7", "texto8"],
     ["texto9", "texto10"],
     ["texto11", "texto12"]]
])

# Imprimir los arrays para verificar los valores asignados
print("Array 2x3x2:")
print(array_2x3x2)
print("/Array 5x5x1:")
print(array_5x5x1)
print("(/Array 3x6x2:")
print(array_3x6x2)
