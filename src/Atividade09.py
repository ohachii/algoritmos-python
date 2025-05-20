soma = 0 
contador = 0 
contador_input = 0  

while contador_input < 4:
    numero = int(input("Digite um número inteiro: "))
    contador_input += 1  

    if numero % 2 == 0:  
        soma += numero 
        contador += 1  

if contador > 0:
    media = soma / contador
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi digitado.")