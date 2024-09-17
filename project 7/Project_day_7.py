import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice (word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for num in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []


while not game_over:
    guess = input("Adivinha a letra: ").lower()
    print(f"Você ainda tem {lives}/6 ainda.")

    if guess in correct_letters:
        print("Você já usou essa Letra!")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)



    if guess not in chosen_word:
        lives -= 1
        print(f"Você escolheu a letra {guess}, ela não esta na palavra, você perdeu uma vida.")
        if lives == 0:
            game_over = True
            print("Voce Perdeu!")
            print(f"A palavra era {chosen_word}!")

    if "_" not in display:
        game_over = True
        print("Voce Ganhou!")
    
    
