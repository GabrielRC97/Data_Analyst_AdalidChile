import numpy as np

#1

matriz1 = np.random.randint(1,10,(3,3))
matriz2 = np.random.randint(1,10,(3,3))

print(matriz1)
print(matriz2)
print(matriz1 + matriz2)

#2

matrizid = np.identity(4)
print(matrizid)

#3

matriz1 = np.random.randint(0,2,(3,3))
print(matriz1)

matriz1 = np.bool_(matriz1)
print(matriz1)

#4

matriz = np.arange(0,101,2)
print(matriz.size)
print(matriz)
