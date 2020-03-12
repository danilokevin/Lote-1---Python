# Objetivo: Receba as notas bimestrais do aluno. Calcule sua média e mostre seu status de acordo com os critérios estabelecidos.

n1=float(input("Nota do 1º bimestre: "))
n2=float(input("Nota do 2º bimestre: "))
n3=float(input("Nota do 3º bimestre: "))
n4=float(input("Nota do 4º bimestre: "))

media=(n1+n2+n3+n4)/4

if (media>=6):
  print("ALUNO APROVADO")
elif (media>=3):
  print("ALUNO EM EXAME")
else:
  print("ALUNO RETIDO")