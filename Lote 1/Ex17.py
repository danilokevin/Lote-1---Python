# Objetivo: Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo
# de percurso e a velocidade média

dist=int(input("Qual a distância em Km até o destino? "))

litros=dist/12
litros = round(litros,2)

tempo=int(input("Qual o tempo do percurso em horas? "))
velm=dist/tempo

print("Será necessário", litros, "litros para a viagem")
print("A velocidade média será de", velm, "km/hora")