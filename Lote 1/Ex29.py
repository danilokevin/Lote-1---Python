# Objetivo: Receba o tipo de investimento (1=POUP rende 3% ou 2=RENDA FIXA rende 5%) e o valor do investimento.
# Demais tipos não serão considerados.

Inv=float(input("Valor da aplicação inicial: R$ "))
Tipo=int(input("Digite 1 para POUPANÇA ou 2 para RENDA FIXA: "))

Resg=float=0

if (Tipo==1):
  Resg=(Inv*1.03)
  print("Valor do resgate após 30 dias: R$", Resg)
elif (Tipo==2):
  Resg=(Inv*1.05)
  print("Valor do resgate após 30 dias: R$", Resg)
else:
  print("Tipo de investimento não reconhecido. Tente novamente!")
