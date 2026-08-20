def escolherjogo():
    print("─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄")
    print("█░░░█░░░░░░░░░░▄▄░██░█")
    print("█░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█")
    print("█░░░▀░░░▄▄▄▄▄░░██░▀▀░█")
    print("─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀")
    print("Escolha o jogo que deseja jogar:")
    print("[1] Jogo da Forca")
    print("[2] Jogodeadivinhação")

    escolha = int(input("Digite o número do jogo que deseja jogar: "))

    match escolha:
        case 1:
            from jogodaforca import jogar
            jogar()
        case 2:
            from jogodeadivinhação import jogar
            jogar()
            escolherjogo()