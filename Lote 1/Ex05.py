# Objetivo: Receber os coeficientes de uma equação de 2º grau e calcular suas raízes, considerando que são reais

import math

A=float(input("Digite o valor de A: "))
B=float(input("Digite o valor de B: "))
C=float(input("Digite o valor de C: "))

D=(B*B)-4*A*C

X1=(-(B+math.sqrt(D))/2*A)
X2=(-(B-math.sqrt(D))/2*A)
print("As raízes são: ", X1, " e ", X2)