# Objetivo: Receba um número inteiro. Calcule e mostre seu fatorial.

N=int(input("Declare um número: "))
cont=1
FAT=1

while cont<=N:
  FAT=(FAT*cont)
  cont+=1
print("O fatorial de", N, "é", FAT)