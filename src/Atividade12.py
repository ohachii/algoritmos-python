cont = 0
palavra=str(input("Digite uma palavra: "))
for letra in palavra:
  if letra in "aeiou":
    cont+=1
print(f"A quantidade de vogais é {cont}")