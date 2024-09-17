alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Digite 'encode' para criptografar ou digite 'decode' para descriptografar!\n")
text = input("Digite a mensagem: \n")
shift = int(input("Digite quantas casas para criptografar: \n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Aqui o resultado da criptografia: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Aqui o resultado da descriptografa: {output_text}")    



if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
else: 
    print("Voce Digitou errado!")




