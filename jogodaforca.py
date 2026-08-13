# Jogo da forca
import random
from desenhojogo import desenhoforca, mensagem_perdedor, mensagem_vencedor

print("*********************************")
print("Bem vindo ao jogo da Forca")
print("*********************************")

# Carrega palavras do arquivo
with open("palavrasecreta.txt", "r", encoding="utf-8") as arquivo:
    palavras = [palavra.strip().upper() for palavra in arquivo.readlines()]

palavrasecreta = random.choice(palavras)
letrasacertadas = ["_"] * len(palavrasecreta)
total_tentativas = 6

enforcou = False
acertou = False 
tentativas = 0
letras_usadas = []

print("A palavra secreta tem {} letras".format(len(palavrasecreta)))
print(desenhoforca(tentativas))
print(" ".join(letrasacertadas))
desenhoforca(tentativas)

while(not enforcou and not acertou):
    chute = input("\nDigite uma letra: ")
    chute = chute.strip().upper()
    
    if not chute or len(chute) != 1 or not chute.isalpha():
        print("Por favor, digite uma letra válida!")
        continue
    
    if chute in letras_usadas:
        print("Você já tentou essa letra!")
        continue
    
    letras_usadas.append(chute)

    if (chute in palavrasecreta):
        index = 0
        for letra in palavrasecreta:
            if(chute == letra):
                letrasacertadas[index] = letra
            index = index + 1
        print("Acertou! A letra '{}' está na palavra.".format(chute))
    else:
        tentativas += 1
        print("Errou! A letra '{}' não está na palavra.".format(chute))

    enforcou = tentativas == total_tentativas
    acertou = "_" not in letrasacertadas
    
    print(desenhoforca(tentativas))
    print(" ".join(letrasacertadas))
    print("Letras usadas:", ", ".join(letras_usadas))
    print("Tentativas restantes:", total_tentativas - tentativas)

# Verifica se o jogador ganhou ou perdeu
if (acertou):
    print("\nParabéns, você ganhou!")
    print("A palavra era: {}".format(palavrasecreta))
    mensagem_vencedor()
elif (enforcou):
    print("\nVocê perdeu!")
    print("A palavra era: {}".format(palavrasecreta))
    mensagem_perdedor(palavrasecreta)

print("Fim do jogo")