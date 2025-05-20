L1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def maiorlista(L1):
  maior = L1[0]  
  for i in range(1, len(L1)):
    if (L1[i] > maior):
      maior = L1[i]
      print(f'maior={L1[i]}')
  return maior  
print(maiorlista(L1))