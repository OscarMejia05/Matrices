


import random

matriz10 = [[0] * 10 for _ in range(10)]
mayor = 0   
for i in range(10):
    for j in range(10):
        matriz10[i][j] = random.randint(1, 100)
        if matriz10[i][j] > mayor:
            mayor = matriz10[i][j]
            posicion = [i, j]   
            
print("Matriz:", {matriz10})
print("El número mayor es:", mayor)
print("La posición del número mayor es:", posicion)