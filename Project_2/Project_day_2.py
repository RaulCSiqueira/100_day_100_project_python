print("Bem Vindo ao gerador de gorgetas! \n")
valor = float(input("Qual o valor da Conta? "))
gorgeta = int(input("Quantos porcento de gorgeta você quer deixar? 10, 12 ou 15? "))
if gorgeta == 10:
    valor = valor * 1.10
elif gorgeta == 12:
    valor = valor * 1.12
elif gorgeta == 15:
    valor = valor * 1.15
pessoas = int(input("Quantas Pessoas vão dividir a conta? "))
total = round((valor/pessoas), 2)
print(f"Valor que cada pessoa vai pagar é: {total}")