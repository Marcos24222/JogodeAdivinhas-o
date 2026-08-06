# Jogo da forca
print("*********************************")
print("Bem vindo ao jogo da Forca")
print("*********************************")

palavrasecreta = "Abacaxi".upper()
letrasacertadas = ["_"] * len(palavrasecreta)

print(palavrasecreta)

enforcou = False
acertou = False
tentativas=0

while (not enforcou and not acertou and tentativas < 5):
    chute = input("Digite uma letra? ")
    chute = chute.strip()

    if(chute in palavrasecreta):
        index = 0
        for letra in palavrasecreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
    else:
        tentativas+=1
        

    print("jogando")

print("Fim do jogo")