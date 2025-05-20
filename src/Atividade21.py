L1=[1,2,3,4,5,6,7,8,9,10]
def menorlista(L1):
  menor_l= L1[0]
  for i in range(1,len(L1)):
    if L1[i]<menor_l:
      menor_l=L1[i]
  return menor_l

print(menorlista(L1))