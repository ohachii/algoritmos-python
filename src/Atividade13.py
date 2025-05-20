numeroint = int(input("Digite um número inteiro de 3 dígitos: "))

primeiro_digito = numeroint // 100 
segundo_digito = (numeroint % 100) // 10 
terceiro_digito = numeroint % 10

soma_dos_digitos = primeiro_digito + segundo_digito + terceiro_digito

print(f"A soma dos dígitos do número {numeroint} é: {soma_dos_digitos}") 