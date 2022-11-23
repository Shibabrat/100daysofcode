# Day 7 project: Hangman

import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# test word list
# word_list = ["aardvark", "baboon", "camel"] 

chosen_word = word_list[random.randint(0,len(word_list)-1)]

display = []
for i in range(len(chosen_word)):
    display.append("_")

print("".join(display))

numTries = 0
wordComplete = False

while numTries <= 6 and wordComplete == False:
    guess = input("Enter your guess letter: ").lower()
    
    if guess in chosen_word:
        for i in range(0,len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
                
        print(''.join(display))
    else:
        numTries += 1
        print(f"Number of tries left: {7-numTries}")
        print(stages[7 - numTries])


    if "_" not in display:
        wordComplete = True
        print("You win!")

    if numTries == 7:
        print(f"I win! The chosen word was {chosen_word}")

    