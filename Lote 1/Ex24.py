# Objetivo: Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

A=int(input("Digite um número: "))
if(A%6)==0:
  print("SIM! É DIVISÍVEL POR 2 E 3")
elif(A%3)==0:
  print("DIVISÍVEL SOMENTE POR 3")
elif(A%2)==0:
  print("DIVISÍVEL SOMENTE POR 2")
else:
  print("NÃO É DIVISÍVEL POR 2 OU 3")