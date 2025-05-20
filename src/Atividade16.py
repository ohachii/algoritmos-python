n1 = float(input("Insira o primeiro valor: "))
n2 = float(input("Insira o segundo valor: "))
n3 = float(input("Insira o terceiro valor: "))
if (n1 > n2) and (n1 > n3):
   print(f"{n1} é o valor mais alto")
if (n2 > n1) and (n2 > n3):
   print(f"{n2} é o valor mais alto")
if (n3 > n1) and (n3 > n2):
   print(f"{n3} é o valor mais alto")
if (n1 < n2) and (n1 < n3):
   print(f"{n1} é o valor menor dentre eles")
if (n2 < n1) and (n2 < n3):
   print(f"{n2} é o valor menor dentre eles")
if (n3 < n1) and (n3 < n2):
   print(f"{n3} é o valor menor dentre eles")