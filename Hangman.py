import random

words_list = ["phthon", "hangman", "challenge", "programming", "computer", ]
def display_word(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display += " "    
    
    return display       

word = random.choice(words_list)
guessed_letters = set()
attempts = 6
while attempts > 0:
    print("Welcom to Hangman Game. ")
    print(f'word : {display_word(word, guessed_letters)} )')
    print(f'Guessed Letter: {" ".join(guessed_letters)}')
    print(f'Attempts Left: {attempts}')

    guess = input("Enter The Letter: ").lower()
    guessed_letters.add(guess)  

    if guess in word:
        print("Good Effort! ")
    else:
        print("Wrong Guess! ")
        attempts -= 1    

    if "_" not in display_word(word, guessed_letters):
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game Over! The correct word was: {word}")
