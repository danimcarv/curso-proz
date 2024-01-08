# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto o número 13.

print("Andares do hotel: ")
for i in range(21) :
  if i == 13 :
    continue
  print(i)

#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

print("Andares do hotel: ")
andar = 0
while andar <= 20 :
  if andar != 13 :
    print(andar)
  andar = andar + 1

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
print("Andares do hotel: ")
for i in range(20,-1,-1) :
  if i == 13 :
    continue
  print(i)
