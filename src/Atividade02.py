L1 = [100, 21, 12, 33, 2, 4, 79, 80, 99, 91]
L2 = [300,400,500,600,700,800,900,1000,2000,3000]
corte = 5  
parte1 = []
parte2 = []
for i, elemento in enumerate(L1):
  if i < corte:
    parte1.append(elemento)
  else:
    parte2.append(elemento)
parte11=[]
parte22=[]
for i, elemento in enumerate(L2):
   if i < corte:
     parte11.append(elemento)
   else:
     parte22.append(elemento)

print("Parte 1 (L1):", parte1)
print("Parte 2 (L1):", parte2)
print("Parte 1 (L2):", parte11)
print("Parte 2 (L2):", parte22)