import random

# Creating a list of words and picking a random one.
words = ["Arizona", "College", "Football", "Homework", "United States", "Mesa", "Python"]
word = random.choice(words)

# Tracking what letters have been guessed and how many attempts are left.
guessed = []
attempts = 6

print("Guess the Word")
print("_" * len(word))

# Keeps going until the word is guessed or there are no more attempts.
while attempts > 0:
    guess = input("Enter a letter: ").lower()

    # Displays a message if the guess was correct or incorrect.
    if guess in word:
        print("Yes, great guess")
    else:
        print("No, sorry that letter is not in the word")
        attempts -= 1

    guessed.append(guess)

    # Shows which correct letters were guessed.
    show_word = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(show_word))

    # Checks to see if the word was completed
    if "_" not in show_word:
        print("Great job, you guessed the word")
        break

    if "_" in show_word:
        print("Sorry, you ran out of attempts. The word was:", word)
           
