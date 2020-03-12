# Objetivo: Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

import math

c1=int(input("Qual o valor do primeiro cateto? "))
c2=int(input("Qual o valor do segundo cateto? "))

hip=math.sqrt((c1*c1)+(c2*c2))

print("O valor da hipotenusa é: ", hip)