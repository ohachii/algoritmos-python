L1 = ["Uma frase muito massa"]
def vogallista(L1):
  vogais = 0  
  for frase in L1:  
    for letra in frase:  
      if letra.lower() in "aeiou": 
        vogais += 1  
return vogais  
print(vogallista(L1))