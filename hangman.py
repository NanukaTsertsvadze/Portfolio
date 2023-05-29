import random

words = ["dog", "cat", "mouse", "girrafe", "leopard", "Lion", "monkey"]

print("Welcome to Hangman Game!")
print("Hope you will have fun.Let's Start The game.")

#Choose a random word from words list.
random_word = random.choice(words).lower()
random_underscores = []

for each in random_word:
    random_underscores.append("_")

# Guessing the word.
game_over = False
guessed_correctly = []
guessed_incorrectly = []
try_amount = 7


while try_amount>0:
    output = ''
    for letter in random_word:
        if letter in guessed_correctly:
            output += letter
        else:
            output+= "_ "
    if output == random_word:
        break
    print("Guess a word", output)
    print(try_amount, "Tries left")
    guess = input("Please, enter letter: ")
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("You have already tried it. Try smthing another")
    elif guess in random_word:
        guessed_correctly.append(guess)
        print("Awesome!You got it right!")
    elif guess not in random_word:
        try_amount -=1
        guessed_incorrectly.append(guess)
        print("Try other letter. Don't Give up")
        if try_amount == 0:
            print("Sorry you lose")
            break
    elif output == random_word:
        print(f"Congrats. You got it right.the word was {random_word}")
        break


