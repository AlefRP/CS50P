import random

# Analyses and print output
def check_value(guess, answer):
    if guess < answer:
        print("Too small!")
        return 0
    elif guess > answer:
        print("Too large!")
        return 0
    else:
        print("Just right!")
        return 1

# Get level from user
while True:
    try:
        level = int(input('Level: '))
        if level >= 1:
            break
    except ValueError:
        pass

# Generate a random integer between 1 and 100
if level > 1:
    answer = random.randrange(1, level)
else:
    answer = 1

# Get guess from user
while True:
    try:
        guess = int(input('Guess: '))
        check = check_value(guess, answer)
        if guess >= 1 and check == 1:
            break
    except ValueError:
        pass



