# Objetivo: Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos

n1=int(input("Qual o ano de nascimento? "))
n2=int(input("Qual o ano atual? "))

idade = (n2-n1)
print("Sua idade atual é", idade, "anos")

idadefut=idade+17
print("Sua idade daqui 17 anos é de", idadefut, "anos")