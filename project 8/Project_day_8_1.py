alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Digite 'encode' para criptografar ou digite 'decode' para descriptografar!\n")
text = input("Digite a mensagem: \n")
shift = int(input("Digite quantas casas para criptografar: \n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
             shift_amount *= -1
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    if encode_or_decode == "encode":
        print(f"Aqui o resultado da criptografia: {output_text}")
    elif encode_or_decode == "decode":
        print(f"Aqui o resultado da descriptografa: {output_text}") 

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
