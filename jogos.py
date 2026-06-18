print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numerosecreto = 40

chute = input("Digite o seu número:  ")
print("você digitou;" ,chute )

chuteNumerico = int(chute)

if(numerosecreto == chuteNumerico):
  print("Você acertou!")
else:
    print("Você errou!")

print("Fim de Jogo")