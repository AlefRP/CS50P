"""
This program is based on the tutorial: "Build a Dice-Rolling Application With Python"
(https://realpython.com/python-dice-roll/), but it has been modified to be
completely different from the original code.
"""

import random
from collections import Counter
from itertools import product

class Die:
    """Represents a six-sided die with ASCII art for each face."""

    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }


    def __init__(self):
        self.value = self.roll()


    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


    def __str__(self):
        return "\n".join(self.DICE_ART[self.value])


def main():
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? [1-6] "))
            validated_num_dice = get_num_dice(num_dice)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            target_sum = int(input("What's your guess for the sum of dice values? "))
            validated_target_sum = get_target_sum(validated_num_dice, target_sum)
            break
        except ValueError as e:
            print(e)

    dice = [Die() for _ in range(validated_num_dice)]
    dice_faces_diagram = generate_dice_faces_diagram(dice)

    probability = calculate_probability(validated_num_dice, validated_target_sum)
    print(f"The probability of getting a sum of {validated_target_sum} with {validated_num_dice} dice is {probability:.2%}")

    print(f"\n{dice_faces_diagram}")

    if sum(die.value for die in dice) == validated_target_sum:
        print("Congratulations! You guessed the correct sum.")
    else:
        print("Sorry, your guess was incorrect.")


def get_num_dice(num_dice):
    """
    Validate the number of dice.

    Args:
        num_dice (int): The number of dice to roll

    Returns:
        int: The validated number of dice to roll, between 1 and 6
    """
    if 1 <= num_dice <= 6:
        return num_dice
    else:
        raise ValueError("Invalid input. Please enter a number from 1 to 6.")


def get_target_sum(num_dice, target_sum):
    """
    Validate the target sum based on the number of dice.

    Args:
        num_dice (int): The number of dice to roll
        target_sum (int): The target sum of the dice roll

    Returns:
        int: The validated target sum of the dice roll
    """
    min_sum = num_dice
    max_sum = num_dice * 6

    if min_sum <= target_sum <= max_sum:
        return target_sum
    else:
        raise ValueError(f"Invalid input. With {num_dice} dice, the sum must be between {min_sum} and {max_sum}.")


def calculate_probability(num_dice, guessed_sum):
    """
    Calculate the probability of getting a specific sum with a given number of dice.

    Args:
        num_dice (int): The number of dice to roll.
        guessed_sum (int): The target sum to calculate the probability for.

    Returns:
        float: The probability of getting the target sum with the given number of dice.
    """
    possible_rolls = list(product(range(1, 7), repeat=num_dice))
    sums = [sum(roll) for roll in possible_rolls]
    counter = Counter(sums)
    return counter[guessed_sum] / len(possible_rolls)


def generate_dice_faces_diagram(dice):
    """
    Generate the ASCII diagram of dice faces.

    Args:
        dice (list): A list of Die objects

    Returns:
        str: The diagram of the dice faces
    """
    dice_faces_rows = [
        " ".join(str(die).split("\n")[row_idx] for die in dice)
        for row_idx in range(len(Die.DICE_ART[1]))
    ]
    width = len(dice_faces_rows[0])
    diagram_header = f"{'~' * 9} RESULTS {'~' * 9}"
    return "\n".join([diagram_header] + dice_faces_rows)


if __name__ == "__main__":
    main()