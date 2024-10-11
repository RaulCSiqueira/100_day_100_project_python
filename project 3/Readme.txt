Day 3 Project: Treasure Island

Project #003: Treasure Hunt

In the third project, we developed a simple game where the goal is to find hidden treasure. The basic mechanics involve using conditional statements to guide the player on their journey to the treasure.

We start with a code that welcomes the player and explains their mission:

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
The first choice asks which direction the player wants to go, "right" or "left." We use the input() function to capture the response and an if statement to define the next step:

step1 = input("Which direction do you want to go? 'right' or 'left'? ")
if step1 == "left":
    # The adventure continues
else:
    print("You lost!")

If the player chooses "left," they move on to the next step. Here, they decide whether to "swim" or "wait" for the boat. If they choose to wait, they proceed. Otherwise, the game ends:


step2 = input("Do you want to 'swim' or 'wait' for the boat? ")
if step2 == "wait":
    # Move on to the final phase
else:
    print("You lost!")

In the third and final step, the player chooses between three doors: "red," "blue," or "yellow." If they choose the yellow door, they win the game:


step3 = input("Which door do you want to enter? 'red', 'blue' or 'yellow'? ")
if step3 == "yellow":
    print("You won!!!")
else:
    print("You lost!")

Here is the complete program:

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")

step1 = input("Which direction do you want to go? 'right' or 'left'? ")
if step1 == "left":
    step2 = input("Do you want to 'swim' or 'wait' for the boat? ")
    if step2 == "wait":
        step3 = input("Which door do you want to enter? 'red', 'blue' or 'yellow'? ")
        if step3 == "yellow":
            print("You won!!!")
        else:
            print("You lost!")
    else:
        print("You lost!")
else:
    print("You lost!")

This project helped me consolidate the use of if and else conditionals, allowing for dynamic interactions and simulating a simple game logic.


Projeto dia 3: Ilha do Tesouro

Projeto #003: Achar o Tesouro

No terceiro projeto, desenvolvemos um jogo simples onde o objetivo é encontrar um tesouro escondido. O funcionamento básico envolve o uso de condicionais para guiar o jogador em sua jornada até o tesouro.

Começamos com um código que dá as boas-vindas ao jogador e explica sua missão:

print("Bem-vindo à ilha do tesouro!")
print("Sua missão é encontrar o tesouro!")

A primeira escolha é para qual direção o jogador deseja ir, "direita" ou "esquerda". Usamos a função input() para capturar a resposta e a estrutura condicional if para definir o próximo passo:

passo1 = input("Qual direção você quer ir? 'direita' ou 'esquerda'? ")
if passo1 == "esquerda":
    # Segue a aventura
else:
    print("Você perdeu!")

Se o jogador escolher "esquerda", ele avança para o próximo passo. Aqui, o jogador decide se vai "nadar" ou "esperar" pelo barco. Se optar por esperar, ele segue adiante. Caso contrário, o jogo termina:

passo2 = input("Você quer ir 'nadando' ou 'esperar' pelo barco? ")
if passo2 == "esperar":
    # Avança para a última fase
else:
    print("Você perdeu!")

No terceiro e último passo, o jogador escolhe entre três portas: "vermelha", "azul" ou "amarela". Se escolher a porta amarela, ele vence o jogo:

passo3 = input("Qual porta você quer entrar? 'vermelha', 'azul' ou 'amarela'? ")
if passo3 == "amarela":
    print("Você ganhou!!!")
else:
    print("Você perdeu!")
Aqui está o programa completo:


print("Bem-vindo à ilha do tesouro!")
print("Sua missão é encontrar o tesouro!")

passo1 = input("Qual direção você quer ir? 'direita' ou 'esquerda'? ")
if passo1 == "esquerda":
    passo2 = input("Você quer ir 'nadando' ou 'esperar' pelo barco? ")
    if passo2 == "esperar":
        passo3 = input("Qual porta você quer entrar? 'vermelha', 'azul' ou 'amarela'? ")
        if passo3 == "amarela":
            print("Você ganhou!!!")
        else:
            print("Você perdeu!")
    else:
        print("Você perdeu!")
else:
    print("Você perdeu!")

Esse projeto me ajudou a consolidar o uso de condicionais if e else, permitindo criar interações dinâmicas e simular uma lógica de jogo simples.
