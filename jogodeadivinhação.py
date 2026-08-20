import random

from jogodaforca import jogar

def jogar():
    print("********************************")
print("Bem-vindo ao Jogo de Adivinhação")
print("********************************")

numerosecreto = random.randint(1, 50)
tentativas_restantes = 0
pontos = 1000

print("Qual o nível de dificuldade você vai escolher?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Digite o número da dificuldade: "))

if nivel == 1:
    tentativas_restantes = 20
    pontos = 1000
elif nivel == 2:
    pontos = 1000
    tentativas_restantes = 10
else:
    pontos = 1000
    tentativas_restantes = 5

while tentativas_restantes > 0:
    print(f"Você tem {tentativas_restantes} tentativas")
    chute = input("Digite o seu número (1-50) ou 'sair' para encerrar: ").strip()

    if chute.lower() == 'sair':
        print("Jogo encerrado pelo jogador.")
        break

    if not chute.isdigit():
        print("Entrada inválida. Digite um número inteiro entre 1 e 50.")
        continue

    chuteNumerico = int(chute)
    if chuteNumerico < 1 or chuteNumerico > 50:
        print("Número fora do intervalo. Digite um número entre 1 e 50.")
        continue

    if chuteNumerico == numerosecreto:
        print("Parabéns! Você acertou! Fim do jogo")
        break
    elif chuteNumerico > numerosecreto:
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")

    tentativas_restantes -= 1
    pontos -= abs(chuteNumerico - numerosecreto)
    pontos = max(pontos, 0)  # Garantir que os pontos não fiquem negativos
    if tentativas_restantes == 0:
        print(f"Você não tem mais tentativas. O número era {numerosecreto}. Fim do jogo.")
        break

print(f"Sua pontuação final é: {pontos}")
jogar ()