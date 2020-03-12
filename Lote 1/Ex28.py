# Objetivo: Receba o preço atual e a venda média mensal de um produto. Calcule seu novo preço de acordo com os
# critérios estabelecidos.

PA=float(input("Preço atual do produto: "))
VMM=int(input("Venda média mensal do produto: "))
NP=0

if (PA<30 and VMM<500):
  NP=PA*1.10
  print("Novo preço: R$", NP)
elif (PA<80 and VMM<1000):
  NP=PA*1.15
  print("Novo preço: R$", NP)
elif (PA>=80 and VMM>=1000):
  NP=PA*0.95
  print("Novo preço: R$", NP)
else:
  print("O produto permanece com seu preço atual: R$", PA)