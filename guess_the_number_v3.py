import random
my_random_number = random.randint(1,100)

print("I am thinking of a number between 1 and 100.")

while True:
    guess = int(input("What's the number? "))

    if guess == my_random_number:
        print("Yes! You win!")
        break
    elif guess < my_random_number:
        print("{} is too low.".format(guess))
    else:
        print("{} is too high.".format(guess))
