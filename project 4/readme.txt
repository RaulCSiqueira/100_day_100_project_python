Day 4 Project: Rock paper scissors

Project #004: Rock, Paper, Scissors Game
On the fourth day, we made a simple Rock, Paper, Scissors game where you choose a number for each option and play against a "computer." In this project, we introduce something new: the use of the import statement. This allows us to bring in code from another module or program to work together with our code. In this case, we're using random to select a random number from a set of options. We won't dive too deeply into the concept that random number generation isn't truly random, but the line looks like this:

import Random

random is a built-in module in Python, so you don't need to install or download it. However, if you want to explore other options, there are many ready-to-use libraries available online. Now, let's move on to the next line, where we display a welcome message to the player using print:

print("Welcome to the Rock, Paper, Scissors game! \n")

Next, we create a variable with an input that prompts the player to choose a number between 0 and 2, where 0 represents Rock, 1 represents Paper, and 2 represents Scissors:

value = float(input("Choose one: 0 for Rock, 1 for Paper, and 2 for Scissors: \n"))

In the next line, we integrate the random module into the program using randint, which generates a "random" choice for the computer from the range 0 to 2:

computer_value = random.randint(0, 2)

Now we use the if and elif statements to compare the player's choice with the computer's. There are many ways to write this section—some are more efficient than others, but if it works, it's not wrong. I've chosen a method that provides a unique response for each combination of player and computer choices:

if value == 0 and computer_value == 2:
    print("You chose Rock!")
    print("Computer chose Scissors!")
    print("You won!")
elif value == 0 and computer_value == 1:
    print("You chose Rock!")
    print("Computer chose Paper!")
    print("Computer won!")
elif value == 0 and computer_value == 0:
    print("You chose Rock!")
    print("Computer chose Rock!")
    print("It's a tie!")
elif value == 1 and computer_value == 0:
    print("You chose Paper!")
    print("Computer chose Rock!")
    print("You won!")
elif value == 1 and computer_value == 1:
    print("You chose Paper!")
    print("Computer chose Paper!")
    print("It's a tie!")
elif value == 1 and computer_value == 2:
    print("You chose Paper!")
    print("Computer chose Scissors!")
    print("Computer won!")
elif value == 2 and computer_value == 0:
    print("You chose Scissors!")
    print("Computer chose Rock!")
    print("Computer won!")
elif value == 2 and computer_value == 1:
    print("You chose Scissors!")
    print("Computer chose Paper!")
    print("You won!")
elif value == 2 and computer_value == 2:
    print("You chose Scissors!")
    print("Computer chose Scissors!")
    print("It's a tie!")
elif value >= 3 or value < 0:
    print("Invalid number. You lost!")

And that’s how we complete another day of Python programming.



Projeto dia 4: jogo de pedra papel e tesoura

Projeto #004: Jogo de pedra papel e tesoura


No quarto dia vamos fazer um jogo simples de Pedra, Papel e Tesoura, onde você vai escolher um número para cada opção e vamos jogar contra um “computador” e nesse primeira linha vamos ver algo que não vimos ainda que o uso do “import” ele vai importar um programa ou uma linha de outro programa para trabalhar em conjunto com o seu programa, nesse programa vamos usar o “random” que serve para escolher um número aleatório dentro de um leque de opções, não vamos entrar em detalhe sobre o a escolha aleatórias do número não ser aleatório, e a linha vai ficar assim,

import random 

o “random” é uma importação que já vem dentro do próprio Python você não precisa baixar ou fazer ele, ele já vem na biblioteca no Python, mas caso você quer fazer um ou baixar tem várias bibliotecas prontas na internet. Assim vamos para a próxima linha que vai aparecer para a pessoa que vai jogar vamos de “print” de boas-vindas,

print("Bem Vindo ao jogo de Pedra, Papel e Tesoura! \n")

e próximo passo vai ser a variável com o input fazendo você escolher um número entre 0 a 2, sendo 0 para pedra, 1 para papel e 2 para tesoura,

valor = float(input("Escolha um, 0 Para Pedra, 1 para Papel e 2 para Tesoura: \n"))

próxima linha vamos integrar o “random” dentro do programa, junto o “randiant” que vai fazer uma escolha “aleatório” dentro de um raio, nesse programa 0 a 2,

computador_valor = random.randint(0, 2)

a próxima parte vamos usar o “if” e “elif”, mas existe vários jeitos de fazer essa parte, podendo ser com menos linhas de programação ou com muitas linhas, se funcionar não existe um jeito errado de fazer, tem um jeito mais eficiente, mas não errada, o jeito que optei vou usar o para cada opção que eu escolher ou computador escolher vai ter uma resposta “diferente”,

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

Assim completamos mais um dia de programação em Python.
