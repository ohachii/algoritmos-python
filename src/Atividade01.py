L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [3, 7, 4, 21, 12, 14, 1, 56, 70, 80]
L3 = []
for i in L1: 
  if i not in L2:  
    L3.append(i)  
print(L3)  