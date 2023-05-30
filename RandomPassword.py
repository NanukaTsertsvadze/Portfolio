import random

letters="abcdefghijklmnopkrstwxyzABCDEFGHIJKLMNOPKRSTWXYZ,.';^&*$%"
while 1:
    amount = int(input("How many password do you want? "))
    characters = int(input("How many characters password should contain: "))
    for x in range(0, amount): 
       password = ""
       for y in range(0, characters):
             random_letter = random.choice(letters)
             password += random_letter
       print(f"Your passord  : {password}")
  