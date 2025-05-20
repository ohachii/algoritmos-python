def separar_substring(string, delimitador):
  substrings = string.split(delimitador)
  return substrings

string = input("Digite uma string: ")
delimitador = input("Digite o delimitador: ")

substrings = separar_substring(string, delimitador)

print("Substrings:")
for substring in substrings:
  print(substring)