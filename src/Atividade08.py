
linhas = 3
colunas = 3

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matriz_diferenca = []

for i in range(linhas):
  linha_diferenca = []
  for j in range(colunas):
    linha_diferenca.append(matriz1[i][j] - matriz2[i][j])
  matriz_diferenca.append(linha_diferenca)

print("Matriz 1:")
for linha in matriz1:
  print(linha)

print("\nMatriz 2:")
for linha in matriz2:
  print(linha)

print("\nMatriz Diferença:")
for linha in matriz_diferenca:
  print(linha)