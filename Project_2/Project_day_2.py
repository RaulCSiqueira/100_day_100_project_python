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
