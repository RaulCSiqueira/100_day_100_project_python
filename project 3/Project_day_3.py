print("Bem Vindo a ilha do tesouro!")
print("Sua missão é encontrar o tesouro!")
passo1 = input("Qual direção voce quer ir? 'direita' ou 'esquerda'? ")
if passo1 == "esquerda":
    passo2 = input("Você quer ir 'nadando' ou 'esperar' pelo barco? ")
    if passo2 == "esperar":
        passo3 = input("Qual porta voce quer entrar? 'vermelha', 'azul' ou 'amarela'? ")
        if passo3 == "amarela":
            print("Voce Ganhou!!!")
        else:
            print("Você perdeu!")
    else:
        print("Você perdeu!")
else:
    print("Você perdeu!")
