# Objetivo: Receba a quantidade de horas trabalhar e o valor por hora. Calcule o salário bruto, subtraia o percentual
# de descontos e acrescente R$ 100,00 por dependente.

hort=float(input("Qual a quantidade de horas trabalhadas? "))
vh=float(input("Qual o valor por hora? "))

salb=hort*vh

percdesc=float(input("Qual o percentual de desconto? "))

salliq=salb*(1-percdesc/100)

dep=int(input("Quantos dependentes possui? "))

salarec=float=salliq+(dep*100)
print("O valor a receber é de: R$", salarec)