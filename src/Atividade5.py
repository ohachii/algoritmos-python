def sao_anagramas(str1, str2):
  return sorted(str1) == sorted(str2)

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if sao_anagramas(string1, string2):
  print(f"'{string1}' e '{string2}' são anagramas.")
else:
  print(f"'{string1}' e '{string2}' não são anagramas.")