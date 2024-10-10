Day 2 Project: Tip Calculator

Project #002: Tip Calculator

The program for the second day remains simple, but we can add a few new functions. It will be a tip calculator. We’ll start with a simple program, beginning with a print statement to display a welcome message:

print("Welcome to the Tip Generator! \n")

Next, we ask for the bill amount using input combined with float, a function that allows Python to accept decimal numbers:

bill = float(input("What is the bill amount? "))

We continue using input, but this time we use int to accept an integer value. This will be the percentage of the tip we want to leave at the restaurant—either 10%, 12%, or 15%:

tip = int(input("What percentage tip would you like to leave? 10, 12, or 15? "))

In the next part, we’ll learn something new: the if statement. In English, if means “if” some condition is true, do this. Whenever there’s an if, we need a “question” or condition. For example, “If you have 10 dollars or more at the store, buy milk”:

if money >= 10:
    milk = True

We also have elif, which stands for “else if.” For example, “If you have 10 dollars, buy milk, but if you have 20 dollars, buy bread”:

if money == 10:
    milk = True
elif money == 20:
    bread = True

In our case, we want to calculate the tip based on the percentage chosen earlier. If the tip is 10%, we multiply the bill by 1.10; if it’s 12%, we multiply by 1.12; and if it’s 15%, we multiply by 1.15. The code looks like this:

if tip == 10:
    bill = bill * 1.10
elif tip == 12:
    bill = bill * 1.12
elif tip == 15:
    bill = bill * 1.15

Now, we’ll ask how many people will split the bill. Again, we use int, because we need the input to be an integer. Without int, the input could be read as a string, which would cause an error during calculations:

people = int(input("How many people will split the bill? "))

Next, we calculate how much each person has to pay. We divide the total amount (including the tip) by the number of people:

total = round((bill / people), 2)

Here, the round function is used to limit the result to two decimal places. This prevents long decimal numbers from appearing, as float can sometimes result in up to eight decimal places. Finally, we print the amount each person will pay, using print and an f-string to include the variable inside the text:

print(f"Each person will pay: {total}")

With just a few lines of code, we’ve created something that can multiply, divide, compare, and give a final answer. Here is the complete program:

print("Welcome to the Tip Generator! \n")
bill = float(input("What is the bill amount? "))
tip = int(input("What percentage tip would you like to leave? 10, 12, or 15? "))
if tip == 10:
    bill = bill * 1.10
elif tip == 12:
    bill = bill * 1.12
elif tip == 15:
    bill = bill * 1.15
people = int(input("How many people will split the bill? "))
total = round((bill / people), 2)
print(f"Each person will pay: {total}")


Projeto do dia 2: Calculadora


Projeto #002: Calculador de gorjeta 

Programa para o segundo dia continua simples, mas podemos colocar algumas funções novas, vai ser uma calculadora de gorjeta, com o programa simples começamos simples, vamos com “print” que vai dar as boas-vindas, 

print("Bem Vindo ao gerador de gorjetas! \n")

Segunda linha colocamos o valor que deu a conta, com um “input” com o “float”, uma função que ajuda o Python aceitar número fracionados, 

valor = float(input("Qual o valor da Conta? "))

Seguimos com o “input” mas dessa vezes vamos usar o ‘int’ com essa função o valor que vai ser aceita se for numero inteiro, que vai ser o % da gorjeta que vamos dar no restaurante, entre 10, 12 ou 15 porcento

gorgeta = int(input("Quantos porcento de gorjeta você quer deixar? 10, 12 ou 15? "))

Nessa próxima parte vamos ver algo que novo nessa parte do curso o “if”, em português seria o “se” se caso acontece faça isso, e sempre que tiver um “if” vamos ter que ter uma “pergunta”, exemplo, se caso for no mercado e tiver 10 reais ou mais compre leite:

if dinheiro >= 10: 
leite = True

Temos também o “elif” vai ser o “ou se”, exemplo, se caso tiver 10 reais compre leite, mas se tiver 20 reais compre pão: 

if dinheiro == 10: 
leite = True 
elif dinheiro == 20: 
pao = True 

Nesse caso como queremos calcular o valor da porcentagem dar gorjeta dependendo de qual porcentagem que colocamos na linha de cima, podemos colocar se caso o valor der 10, multiplica o valor da conta vezes 1.10, ou se caso o valor for 12, multiplicar o valor da conta por 1.12, ou se caso o valor for 15, multiplicar o valor da conta por 1.12 nas linhas de códigos vai ficar assim: 

if gorjeta == 10:
    valor = valor * 1.10
elif gorjeta == 12:
    valor = valor * 1.12
elif gorjeta == 15:
    valor = valor * 1.15

de fato, vamos colocar quantas pessoas vão dividir a conta, vamos fazer o “input” com “int” lembrando que o “int” é usado para que o número usado na variável seja de fato um número, porque caso for usar ser colocado o “int” a variável vai ler como fosse uma letra, e quando for usado para fazer alguma conta matemática vai dar erro,

pessoas = int(input("Quantas Pessoas vão dividir a conta? "))

Próxima linha, vamos usar para calcular o valor que cada pessoa vai ter que pagar, temos o valor com a gorjeta, divido pelo número de pessoas, 

total = round((valor/pessoas), 2)

nessa parte usamos no final “, 2” essa função é usada para colocar o número de casas que vamos usar após a virgula, por causa que usamos o “float”, esse número pode dar um número com até 8 casas após a virgula e por final vamos imprimir o valor que cada pessoa vai ter que pagar, usando o “print” e o “f” no começo para poder ter de usar uma variável dentro do texto:

print(f"Valor que cada pessoa vai pagar é: {total}")

Assim com junção de apenas algumas linhas de programação já temos algo que pode multiplicar, dividir, fazer comparação e dar a repostar.  O programa completo ficou assim 

print("Bem Vindo ao gerador de gorjetas! \n")
valor = float(input("Qual o valor da Conta? "))
gorjeta = int(input("Quantos porcento de gorjeta você quer deixar? 10, 12 ou 15? "))
if gorjeta == 10:
    valor = valor * 1.10
elif gorjeta == 12:
    valor = valor * 1.12
elif gorjeta == 15:
    valor = valor * 1.15
pessoas = int(input("Quantas Pessoas vão dividir a conta? "))
total = round((valor/pessoas), 2)
print(f"Valor que cada pessoa vai pagar é: {total}")



