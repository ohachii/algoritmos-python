matriz = []


for i in range(4):
  linha = []
print(f"Digite os elementos da linha {i+1}:")
for j in range(7):
   elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
linha.append(elemento)
matriz.append(linha)


menor = matriz[0][0]
linha_menor = 0

for i in range(4):
     for j in range(7):
        if matriz[i][j] < menor:
          menor = matriz[i][j]
        linha_menor = i

maior = matriz[linha_menor][0] 
coluna_maior = 0

for j in range(1, 7):  
   if matriz[linha_menor][j] > maior:
    maior = matriz[linha_menor][j]
    coluna_maior = j


print(f"MINMAX: {maior}")
print(f"Posição (linha, coluna): ({linha_menor + 1}, {coluna_maior + 1})")