nomeCompleto = input("Digite seu nome completo\n")
anoCorreto = False

while anoCorreto == False :
  try :
    anoNascimento = int(input("Digite o ano em que você nasceu \nAnos suportados: de 1922 a 2021\n"))
    if anoNascimento < 1922 or anoNascimento > 2021 :
      print ("O ano informado não está dentro da faixa de valores aceita.")
    else :
      print(nomeCompleto + ", você completará " + str(2022 - anoNascimento) + " anos em 2022!")
      anoCorreto = True
  except :
    print("Caractere inválido inserido!")
