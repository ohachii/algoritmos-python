def criptografar(texto, chave):
  texto_criptografado = ''
  for i, letra in enumerate(texto):
    indice_chave = i % len(chave)  
    chave_letra = chave[indice_chave]

    novo_codigo = ord(letra) + ord(chave_letra)

    nova_letra = chr(novo_codigo)

    texto_criptografado += nova_letra

  return texto_criptografado

texto = input("Digite o texto: ")
chave = input("Digite a chave: ")

texto_criptografado = criptografar(texto, chave)
print("Texto criptografado:", texto_criptografado)