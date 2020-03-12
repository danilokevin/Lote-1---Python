# Objetivo: Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

A=int(input("Digite o primeiro número: "))
B=int(input("Digite o segundo número: "))
C=int(input("Digite o terceiro número: "))
D=int(input("Digite o quarto número: "))

if (D<A):
  print("Os números em ordem crescente são: ", D, ",", A, ",", B, "e", C)
elif (D<B):
  print("Os números em ordem crescente são: ", A, ",", D, ",", B, "e", C)
elif (D<C):
  print("Os números em ordem crescente são: ", A, ",", B, ",", D, "e", C)
else:
  print("Os números em ordem crescente são: ", A, ",", B, ",", C, "e", D)