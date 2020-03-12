# Objetivo: Receba 3 coeficientes A, B, e C de uma equação do 2º grau. Verifique e mostre a existência de raízes reais
# e se caso exista, calcule e mostre.

import math
A=float(input("Digite o valor de A: "))
B=float(input("Digite o valor de B: "))
C=float(input("Digite o valor de C: "))
D=(B*B)-4*A*C
if (D<0):
  print("A equação NÃO POSSUI RAÍZES")
else:
  X1=(-(B+math.sqrt(D))/2*A)
  X2=(-(B-math.sqrt(D))/2*A)

if (D>0):
  print("As raízes são: ", X1, " e ", X2)
if (D==0):
  print("A equação possui apenas 1 raíz:", X1)