# Importing Random module for choosing random word
import random

# List of words
word_list = ["light",
             "aftershock",
             "mango",
             "algorithm",
             "rice",
             "rose",
             "background",
             "consumable",
             "duplicate",
             "python"]

word = random.choice(word_list)  # selecting random word from the list

blank_list = []  # creating a blank list for displaying words with empty letters
for a in word:
    blank_list.append("_")

print(f"{' ':{'*'}^60}")
print(f"{'WELCOME TO THE HANGMAN GAME':{' '}^60}")
print(f"{' ':{'*'}^60}")
name = input("Enter player name:- ")  # Taking name of player
print()
print(f"{f'Welcome {name}':{' '}^60}")
print()
print(f"{' ':{'*'}^60}")  # Instructions of the game
print("!!!Read all the instructions carefully!!!"
      "\nInstructions of the game:-"
      "\n\n01. You will have to guess word from entering letters one by one."
      "\n02. Enter only one letter at a time."
      "\n03. Don't enter numbers, symbols or multiple letters at a time."
      "\n04. Each word is made up of unique letters and there is no repetition of same letter within the word."
      "\n05. Don't enter a letter again if it was already matched with word."
      "\n06. You have 6 chances to complete the game."
      "\n07. For every wrong answer your chances will be decreased by 1."
      "\n08. For every correct answer your chances will remain same."
      "\n09. If you guessed the word within chances then you will won the game."
      "\n10. If you exhaust your all chances then you will lose the game.")
print(f"{' ':{'*'}^60}")

guesses = 6  # number of chances player have
guessed_letters = [] # Track letters already guessed

# loop for running code again and again
while guesses > 0:
    print(f"\nWord to guess: {' '.join(blank_list)}")
    guess_letter = input("Enter a letter : ").lower()  # taking any one letter from the user
    
    # Validation for Rules 2 & 3 (Must be a single alphabetical letter)
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("\nInvalid input! Please enter exactly ONE alphabetic letter.")
        continue
        
    # Validation for Rule 5 (Preventing duplicate guesses)
    if guess_letter in guessed_letters:
        print(f"\nYou already guessed '{guess_letter}'. Try a different letter!")
        continue
        
    guessed_letters.append(guess_letter)

    # Applying conditions according to rules of game
    if guess_letter in word:
        print(f"\nCongratulations {name}, you have guessed a letter of the word")
        for a in range(len(word)):
            if word[a] == guess_letter:
                blank_list[a] = guess_letter
        print(f"Chances left : {guesses}")
        
    else:
        guesses -= 1
        print(f"\nWrong guess!!!\nNow you have only {guesses} choices left")

    # Check if win condition is met
    if "_" not in blank_list:
        print(f"\nCongratulations {name}, You have won the game!")
        print(f"The word was: {word.upper()}\n")
        print(f"{' ':{'*'}^60}")
        break

# If user runs out of guesses
if guesses == 0:
    print(f"\n{' ':{'*'}^60}")
    print("!!!Game Over!!!\nYou have lost the game.")
    print(f"'{word}' was the word.\n")
    print(f"{' ':{'*'}^60}")