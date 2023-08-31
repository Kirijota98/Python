matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

# for i, fila in enumerate(matriz):
#     for j, columna in enumerate(fila):
#         if columna % 2 != 0:
#            matriz[i][j] = 1
#         else:
#            matriz[i][j] =  0
# print(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] % 2 != 0:
           matriz[i][j] = 1
        else:
           matriz[i][j] =  0
print(matriz)
