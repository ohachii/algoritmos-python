frase = input("Digite uma frase: ")
caractere_novo = input("Digite o substituto das letras: ")
nova_frase = ''
for letra in frase:
    if letra.isalpha():
        nova_frase += caractere_novo 
    else:
        nova_frase += letra 
print(f"A nova frase é: {nova_frase}")