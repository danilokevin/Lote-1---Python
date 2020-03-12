# Objetivo: Receba valor de N. Calcule a série 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

N=int(input("Declare um número: "))
F=1
RES=0

for N in range (N, 0, -1):
  X=N
  while X>=1:
    F=(F*X)
    X=(X-1)
  RES=(RES+1/F)
  F=1
RES=(RES+1)
RES=round(RES, 2)
print(RES)
