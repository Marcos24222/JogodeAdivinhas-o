import random

print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numerosecreto = random.randint(1, 50)
tentativas = 10

acertou = False

while tentativas > 0:
    print("Você tem", tentativas, "tentativas.")
    chute = input("Digite o seu número: ")
    print("Você digitou:", chute)
    try:
        chuteNumerico = int(chute)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if chuteNumerico == numerosecreto:
        print("Parabéns! Você acertou! Fim de jogo")
        acertou = True
        break

    if chuteNumerico > numerosecreto:
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")

    tentativas -= 1
    print("Tentativas restantes:", tentativas)

if not acertou:
    print("Fim de jogo. O número secreto era", numerosecreto)
