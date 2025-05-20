frase = str(input("Digite uma frase: "))
alfabeto = "abcdefghijklmnopqrstuvwxyz"
cont = 0

for letra in alfabeto:
  if letra not in frase and letra.upper() not in frase:
   cont += 1

if cont == 0:
 print("A frase é um pangrama")
else:
 print("A frase não é um pangrama")