Day 1 Project: band Name Generator
Projeto dia 1: Gerador de nome de Banda

No primeiro dia aprendemos que Python é uma linguagem de programação orientada a objetos, que a grosso modo podemos colocar tudo como se fosse um objeto, por exemplo, se vamos falar sobre um vaso, o objeto é um vaso, o vaso pode ter na descrição cor, tamanho, marca e ano de produção, entre outras descrições tudo depende como você quer colocar sobre o objeto. Na primeira parte prática do curso aprendemos como funciona variáveis, que ser para guardar “valores” podendo ser números letras dependendo do programa até imagens.


O exercício do primeiro dia vai ser um gerador de nome de banda bem simples, aonde o programa vai das boas-vindas, perguntar de que cidade você cresceu e qual o nome do seu animal de estimação e vai imprimir a junção dos dois valores. 


Para imprimir as boas-vindas, o comando usado é “print” ele vai ser usado para imprimir o que tiver após o comando, por exemplo, se você quiser imprimir a seguinte frase “Hello, World” (CLARO QUE VOU USAR ESSE COMANDO KKKKKK) você vai usar o seguinte comando “print(“Hello, World”)” (exemplo na Imagem 1). Mas se caso vai usar para imprimir o valor de uma variável vou mostrar mais para frente o uso do “print” para variável.


Então o primeiro passo para o exercício é fazer o seguinte comando 

print(“Bem Vindo ao gerador de Nome de Bandas!”)

Segundo passo vai ser perguntar o nome da cidade onde você cresceu, e guardar esse valor em uma variável, para você deixar o valor da variável para o usuário colocar vamos usar o comando de “input(“”)” nesse comando ele vai servi quase como o comando de “print” ele vai imprimir o estiver dentro do “” e vai guardar o valor dentro de uma variável, mas se você apenas colocar o comando “input” apenas assim:

input("Que cidade você cresceu? ")

ele vai guardar o valor em um lugar apenas o computador vai saber, vai usar um valor X na memoria do computador, mas se você guardar o dentro de uma variável que você já deu um nome, sabemos onde vai estar o nome por exemplo:

cidade = input("Que cidade você cresceu? ")

o nome da cidade vai estar dentro da variável “cidade”. (demostrado na imagem 2)

Assim a próxima parte é perguntar o nome do seu animal de estimação, que vai funcionar do mesmo jeito que o nome da cidade com o comando “input” e salvando dentro de uma variável:

animal = input("Qual o nome do seu animal de estimação? ")

mostrando o resultado na imagem 3, lembrando o “print” usado após o comando de “input” e apenas usado para mostrar que o valor guardado dentro da variável está sendo gravado corretamente.

Próximo etapa e imprimir os dois valores juntos com um frase, vamos usar o comando “print” novamente, mas vai ter que fazer alguma alterações para o valor funcionar corretamente, para você usar variáveis dentro de um texto, a varias maneiras de usar, mas o jeito mais fácil e usando “print(f”{variável}”)” assim a variável vai ser colocado dentro do texto se caso você mudar o valor da variável não vai ser necessário mudar no comando do print. Assim essa linha de comando vai ficar assim:

print(f"O nome da sua banda vai ser {cidade} {animal}!!")

assim o programa completo vai ser mostrado na imagem 4.

Assim podemos ver com apenas poucas linhas de comandos podemos fazer um programa, não tem uso prática, mas sim uso didático.
