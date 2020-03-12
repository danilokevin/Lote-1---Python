# Objetivo: Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (em minutos). Calcule e mostre a velocidade média em km/h.

VOLTAS=int(input("Voltas: "))
EXT=int(input("Extensão do circuito em metros: "))
TEMPO=int(input("Duração do circuito em minutos: "))

VelocMed=((VOLTAS*EXT)/1000)/(TEMPO/60)
print("A velocidade média é de: ", VelocMed, "km/h")
