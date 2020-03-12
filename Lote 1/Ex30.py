# Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a idade em anos, meses e dias,
# considerando os anos bissextos.

dias = float = 0
meses = 0
anos = 0


diaNasc=int(input("Dia Nascimento: "))
mesNasc=int(input("Mês Nascimento: "))
anoNasc=int(input("Ano Nascimento: "))
diaAtual=int(input("Dia Atual: "))
mesAtual=int(input("Mês Atual: "))
anoAtual=int(input("Ano Atual: "))

anoNasc += 1
anoAtual -= 1

while (anoNasc < anoAtual):
    if (anoNasc % 4 == 0 and anoNasc % 400 == 0 and anoNasc % 100 != 0):
        dias += 366
    else:
        dias += 365
    anoNasc += 1


dias += (12 - mesNasc) * 30.41
dias += (30.41 - diaNasc)

dias += (mesAtual-1)*30.41
dias += diaAtual

anos = dias/365

meses = anos*12

print("Você já viveu: ")
print(dias, " dias")
print("Ou ", meses, " meses")
print("Ou ", anos + 1, " anos")
