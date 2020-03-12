# Objetivo: Receba dois números. Calcule e mostre o resultado da soma dos números ímpares entre eles.

X=int(input("Declare um número: "))
Y=int(input("Declare outro número: "))
RES=0

if(X<Y):
  if(X%2==0):
    X=(X+1)
  while X<=Y:
      RES=(RES+X)
      X=(X+2)
else:
  if(Y%2==0):
    Y=(Y+1)
  while Y<=X:
    RES=(RES+Y)
    Y=(Y+2)
      
print("O resultado da soma dos números ímpares entre estes dois números é igual a", RES)