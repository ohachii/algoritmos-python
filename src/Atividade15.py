produto = float(input("Insira o valor do produto: ")) 
if produto <= 100:
    desconto = produto * 0.95 
elif produto <= 500:
    desconto = produto * 0.90 
else:
    desconto = produto * 0.85 
print(f"O preço do produto com desconto é: R${desconto:.2f}")
