# Objetivo: Receber dois números reais. Calcule e mostre a diferença entre eles.

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
if (n1<n2):
  dif=n2-n1
else:
  dif=n1-n2

print("A diferença entre os dois números é: ", dif)