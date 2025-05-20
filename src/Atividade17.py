n = int(input("Digite um número: "))
multiplo3 = int(n / 3)
multiplo5 = int(n / 5)
print(multiplo3, multiplo5)
if multiplo3 == int(multiplo3):
  print("O número é múltiplo de 3")
else:
  print("Esse número não é múltiplo de 3")
if multiplo5 == int(multiplo5):
  print("O número é multiplo de 5")
else:
  print("Esse número não é multiplo de 5")