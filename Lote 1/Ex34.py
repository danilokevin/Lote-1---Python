# Objetivo: Calcule e mostre a tabuada de um número recebido.

N=int(input("Declare um número: "))
cont=0

while cont<=10:
  print(N, "X", cont, "=", cont*N)
  cont+=1