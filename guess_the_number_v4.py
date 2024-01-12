import random

my_random_number = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")
num_guesses = 0
max_guesses = 5
remaining_guesses = max_guesses  # Initialize the remaining guesses

while num_guesses < max_guesses:
    guess = int(input("What's the number? "))

    num_guesses += 1
    remaining_guesses -= 1  # Decrement the remaining guesses

    if guess == my_random_number:
        print("Yes! You win!")
        break
    elif guess < my_random_number:
        print("{} is too low. You have {} guesses left.".format(guess, remaining_guesses))
    else:
        print("{} is too high. You have {} guesses left.".format(guess, remaining_guesses))

    if num_guesses == max_guesses:
        print("Sorry, you're out of guesses. The correct number was {}.".format(my_random_number))
