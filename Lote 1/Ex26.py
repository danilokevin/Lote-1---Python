# Objetivo: Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor

X=int(input("Digite o primeiro número: "))
Y=int(input("Digite o segundo número: "))
if (X>Y):
  if (X%Y==0):
    print(X, "é múltiplo de", Y)
  else:
    print(X, "NÃO é múltiplo de", Y)
else:
  if (Y%X==0):
    print(Y, "é múltiplo de", X)
  else:
    print(Y, "NÃO é múltiplo de", X)