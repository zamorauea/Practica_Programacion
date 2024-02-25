# Declaration de variables multidimensional
array_2x3x2 = [[[0, 1], [2, 3], [4, 5]], [[6, 7], [8, 9], [10, 11]]]
array_5x5x5 = [[[x + y * 5 + z * 25 for z in range(5)] for y in range(5)] for x in range(5)]
array_3x6x2 = [[[x + y * 3 + z * 18 for z in range(2)] for y in range(6)] for x in range(3)]

# Impression de los valores de las variables
print("Array 2x3x2:")
for x in array_2x3x2:
    for y in x:
        print(y)
    print()

print("Array 5x5x5:")
for x in array_5x5x5:
    for y in x:
        print(y)
    print()

print("Array 3x6x2:")
for x in array_3x6x2:
    for y in x:
        print(y)
    print()
