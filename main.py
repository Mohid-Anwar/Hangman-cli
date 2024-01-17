import random
from SeectedWord import wordselector

play_again = "y"
while play_again == "y":
    lives = 3
    word = wordselector()
    guessed = False
    correct_letter_guessed = []
    while len(correct_letter_guessed) < 3:
        letter_appender = random.choice(word)
        if letter_appender not in correct_letter_guessed:
            correct_letter_guessed.append(letter_appender)

    status = ""
    index = [index for index in range(0, len(word))]
    print("-------------------welcome to hangman-------------------\n\n".title())

    for letter in word:
        if letter in correct_letter_guessed:
            status += letter
        else:
            status += "_"
    print(status)

    for dis in range(0, len(word)):
        print(index[dis], end="")
    print("\n")
    print(f"Your current lives are : {lives}")

    while not guessed and lives > 0:

        letter_guess = input("Enter one Character or full word: ").lower()

        if len(letter_guess) == 1:
            if not letter_guess.isalpha():
                print("Invalid Character\n")
            elif letter_guess not in word:
                print("This letter is not in word\n")
                lives -= 1
            elif letter_guess in word:
                if letter_guess in correct_letter_guessed:
                    print("Already Guessed")
                else:
                    print("Correct letter guessed\n")

                    correct_letter_guessed.append(letter_guess)
        elif len(letter_guess) == len(word):
            if letter_guess == word:
                guessed = True

            else:
                print("Incorrect attempt at word\n")
                lives -= 1
        else:
            print("Not the same length as guessed word\n")
        status = ""
        if not guessed:
            for letter in word:
                if letter in correct_letter_guessed:
                    status += letter
                else:
                    status += "_"
            print(status)
            for dis in range(0, len(word)):
                print(index[dis], end="")
            print("\n")
            print(f"Your current lives are : {lives}")
        if status == word or guessed:
            guessed = True
            print("Congrats on guessing word!!!\n")
            play_again = input("Do you want to play again? y or n ").lower()
        elif lives == 0:
            print("Out of Lives\nThe word was", word)
            play_again = input("Do you want to play again? y or n ").lower()
else:
    print("\nThank You for Playing Hangman. Goodbye")
