secret_word= "python"
try_count= 0
guess = ""

for letter in secret_word:
    guess += "_ "
    print("Welcome to the Guess the Word Game!")
    print()

while "_ " in guess:
    print(f"Your hint is:{guess}")
    letter_guess = input("What is your guess? ")
    try_count += 1
    print()

    if letter_guess == secret_word:
        guess = secret_word
        break

    new_guess = ""
    for i in range(len(secret_word)):
        if letter_guess == secret_word[i]:
            new_guess += secret_word[i] + " "
        elif guess[i * 2] != "_":
            new_guess += guess[i * 2] + " "
        else:
            new_guess += "_ "

    guess = new_guess

print(f"Congratulations! You guessed the word '{secret_word}' in {try_count} tries.")