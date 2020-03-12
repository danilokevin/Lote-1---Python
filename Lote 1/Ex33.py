# Objetivo: Receba um número inteiro. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N

N=int(input("Declare um número: "))
cont=1
res=0

while cont<=N:
  res=(res+1/cont)
  res=round(res,3)
  cont+=1

print("O resultado da soma da série é: ", res)