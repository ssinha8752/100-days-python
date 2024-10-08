import random

word_list=['aardvark','baboon','camel']

selected_word=random.choice(word_list)

game_over=False
correct_letters=[]

print(selected_word)

while not game_over:
    guess = input("Guess the word?").lower()


    placeholder = ''.join("_" for i in selected_word)
    print(placeholder)

    display = ""
    for i in selected_word:
        if i == guess:
            display += guess
            correct_letters.append(guess)
        elif i in correct_letters:
            display+=i
        else:
            display += ('_')

    print(display)

    if "_" not in display:
        game_over=True
        print("You Win!")