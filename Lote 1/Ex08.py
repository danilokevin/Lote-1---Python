# Objetivo: Receber valor de um depósito em poupança e verificar seu novo valor após 1 mês de aplicação a uma taxa de 1,3% a.m

d=float(input("Qual o valor de depósito realizado? "))
montante=(d*(1+(1.3/100)))
print("O valor atualizado é de: ", montante)