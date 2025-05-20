L1 = [8, 6, 2, 3, 4, 4, 6, 7, 8, 9, 10]


def maiorlista(L1):
  maior = L1[0]
  for i in range(1, len(L1)):
    print(f'{L1[i]} > {maior}')
    if (L1[i] > maior):
      maior = L1[i]
      print(f'maior = {L1[i]}')
  return maior
print(maiorlista(L1))