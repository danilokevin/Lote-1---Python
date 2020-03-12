# Objetivo: Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

N1=int(input("Digite o primeiro número: "))
N2=int(input("Digite o segundo número: "))

if (N1<N2):
  print("Os números em ordem crescente são: ", N1, "e", N2)
else:
  print("Os números em ordem crescente são: ", N2, "e", N1)