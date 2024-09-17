import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem Vindo ao Gerador de senha!")
nr_letters= int(input("Quantas Letras voce quer que sua senha tenha?\n")) 
nr_symbols = int(input(f"Quantos simbolos voce quer?\n"))
nr_numbers = int(input(f"Quantos numeros voce quer?\n"))

password_list = []

for num in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for num in range(1, nr_symbols + 1):
    password_list += random.choice(numbers)
for num in range(1, nr_numbers + 1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for num in password_list:
    password += num

print(f"Seu Password é: {password}")