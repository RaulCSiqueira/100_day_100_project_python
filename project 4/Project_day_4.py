import random


print("Bem Vindo ao jogo de Pedra, Papel e Tesoura! \n")
valor = float(input("Escolha um, 0 Para Pedra, 1 para Papel e 2 para Tesoura: \n"))
computador_valor = random.randint(0, 2)

if valor == 0 and computador_valor == 2:
    print("Você Escolheu Pedra!")
    print("Computador escolher Tesoura!")
    print("Você Ganhou!")
elif valor == 0 and computador_valor == 1:
    print("Você Escolheu Pedra!")
    print("Computador escolher Papel!")
    print("Computador Ganhou!")
elif valor == 0 and computador_valor == 0:
    print("Você Escolheu Pedra!")
    print("Computador escolher Pedra!")
    print("Empataou!")
elif valor == 1 and computador_valor == 0:
    print("Você Escolheu Papel!")
    print("Computador escolher Pedra!")
    print("Você Ganhou!")
elif valor == 1 and computador_valor == 1:
    print("Você Escolheu Papel!")
    print("Computador escolher Papel!")
    print("Empatou!")
elif valor == 1 and computador_valor == 3:
    print("Você Escolheu Papel!")
    print("Computador escolher Tesoura!")
    print("Computador Ganhou!")
elif valor == 2 and computador_valor == 0:
    print("Você Escolheu Tesoura!")
    print("Computador escolher Pedra!")
    print("computador Ganhou!")
elif valor == 2 and computador_valor == 1:
    print("Você Escolheu Tesoura!")
    print("Computador escolher Papel!")
    print("Você Ganhou!")
elif valor == 2 and computador_valor == 2:
    print("Você Escolheu Tesoura!")
    print("Computador escolher Tesoura!")
    print("Empatou!")
elif valor >= 3 or valor < 0:
    print("Numero errado Você Perdeu!")
