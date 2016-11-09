# Jogo da Adivinhação - Parte1

num = 0

def JogoAdivinhacao(num):

    import random

    num = random.randint(1,100)
    numUsuario = int(input("Digite um número entre 1 e 100: "))
    aux = 1
    for i in range(1,3):
        if (num == numUsuario):
            print("Parabéns! Você venceu!")
        elif (num > numUsuario):
            print("Ops, o número é maior que este.")
        elif (num < numUsuario):
            print("Ops, o número é menor que este.")

        numUsuario = int(input("Digite outro número entre 1 e 100: "))
        
        if(num != numUsuario):
            aux += 1
        if (aux == 3):
            print("")
            print("GAME OVER")
            print("O número era", num)

            print("")
            print("Digite 1 para JOGAR NOVAMENTE ou 2 para SAIR")
            opc = int(input(""))
            if (opc == 1):
                JogoAdivinhacao(num)
            else:
                print("Jogo Encerrado!!")

def menu():
    print("Digite 1 para JOGAR ou 2 para INSTRUÇÕES")
    opcPrincipal = int(input(""))
    if (opcPrincipal == 1):
        JogoAdivinhacao(num)
    else:
        print("Olá, Bem vindo ao nosso jogo da Adinhação.")
        print("O jogo funciona assim, um número é aleatoriamente sorteado entre 1 e 100, e você vai ter que adivinhar qual é,")
        print("Você terá apenas 3 chances.")
        print("BOA SORTE!!")

        print("")
        print("Digite 1 para JOGAR ou 2 para SAIR")
        opcInstrucoes = int(input(""))
        if (opcInstrucoes == 1):
            JogoAdivinhacao(num)
        else:
            print("Jogo Encerrado!!")
menu()
