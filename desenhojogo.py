def desenhar_forca(tentativas):
    print("  _______")
    print(" |/      |")
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    if tentativas == 1:
        print(" |      (_)")
        print(" |")
        print(" |")
        print(" |")

    elif tentativas == 2:
        print(" |      (_)")
        print(" |      \\")
        print(" |")
        print(" |")

    elif tentativas == 3:
        print(" |      (_)")
        print(" |      \\|")
        print(" |")
        print(" |")

    elif tentativas == 4:
        print(" |      (_)")
        print(" |      \\|/")
        print(" |")
        print(" |")

    elif tentativas == 5:
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |")

    elif tentativas == 6:
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      /")

    elif tentativas == 7:
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")

    print(" |")
    print("_|___")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________")
    print("   /               \\")
    print("  /                 \\")
    print("//                   \\/\\")
    print("\\|   XXXX     XXXX   | /")
    print(" |   XXXX     XXXX   |/")
    print(" |   XXX       XXX   |")
    print(" |                   |")
    print(" \\__      XXX      __/")
    print("   |\\     XXX     /|")
    print("   | |           | |")
    print("   | I I I I I I I |")
    print("   |  I I I I I I  |")
    print("   \\_             _/")
    print("     \\_         _/")
    print("       \\_______/")


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________")
    print("      '._==_==_=_.'")
    print("      .-\\:      /-.")
    print("     | (|:.     |) |")
    print("      '-|:.     |-'")
    print("        \\::.    /")
    print("         '::. .'")
    print("           ) (")
    print("         _.' '_.")
    print("        '-------'")

