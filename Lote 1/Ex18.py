# Objetivo: Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menos valor

N1=int(input("digite o primeiro número: "))
N2=int(input("digite o segundo número: "))

if (N1>N2):
  dif=N1-N2
else:
  dif=N2-N1

print("A diferença do maior para o menor é de: ", dif)