matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def soma_matriz(matriz):
  soma=0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if i == j:
        soma+=matriz[i][j]

  return soma
print(soma_matriz(matriz))