# Objetivo: Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a
# pessoa consome 50g ao dia.

kg=float(input("Quantos kilos de alimento você possui? "))

dias=int((kg*1000)/50)

print("O alimento durará", dias, " dias")