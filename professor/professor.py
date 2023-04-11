import random
import math

# Main function
def main():
    level = get_level()
    score = 0
    tries = 1
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = (x + y)
        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == result:
                    score += 1
                    break
                elif tries == 3:
                    tries = 0
                    print(f"{x} + {y} = {result}")
                    break
                else:
                    tries += 1
                    print("EEE")
            except ValueError:
                pass
    print("Score:", score)
# Get level from user
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            pass

# Generate integer accordingly to level
def generate_integer(level):
    lower_bound = pow(10, level - 1)  # The smallest n-digit number is 10^(n-1)
    upper_bound = pow(10, level) - 1  # The largest n-digit number is 10^n - 1
    # Generate a random integer between 1 and n(level)
    if level > 1:
        answer = random.randrange(lower_bound, upper_bound)
    else:
        answer = random.randint(0, 9)
    return answer


if __name__ == "__main__":
    main()