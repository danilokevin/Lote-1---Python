# Objetivo: Receba a hora inicial e final de um jogo (em horas e minutos). Calcule a duração do jogo sabendo que: Pode
# ter começado em um dia e terminado no outro, e a duração máxima é de 24 horas.

HI=int(input("Hora inicial do jogo: "))
MI=int(input("Minuto inicial do jogo: "))
HF=int(input("Hora final do jogo: "))
MF=int(input("Minuto final do jogo: "))
if (HI==HF):
  if (MI<MF):
    DURM=(MF-MI)
    print("O jogo durou", DURM, "minutos")
  elif (MI>MF):
    DURH=23
    DURM=(60-MI)+MF
    print("O jogo durou", DURH, "horas e", DURM, "minutos")
  else:
    print("O jogo durou 24 horas")
elif (HI<HF):
  if(MI==MF):
    DURH=(HF-HI)
    print("O jogo durou", DURH, "horas")
  elif (MI<MF):
    DURH=(HF-HI)
    DURM=(MF-MI)
    print("O jogo durou", DURH, "horas e", DURM, "minutos")
  else:
    DURH=(HF-HI)-1
    DURM=(60-MI)+MF
    print("O jogo durou", DURH, "horas e", DURM, "minutos")
else:
  if (MI==MF):
    DURH=(24-HI)+HF
    print("O jogo durou", DURH, "horas")
  elif (MI<MF):
    DURH=(24-HI)+HF
    DURM=(MF-MI)
    print("O jogo durou", DURH, "horas e", DURM, "minutos")
  else:
    DURH=((24-HI)+HF)-1
    DURM=(60-MI)+MF
    print("O jogo durou", DURH, "horas e", DURM, "minutos")