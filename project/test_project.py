import pytest
from itertools import product
from collections import Counter
from project import Die, get_num_dice, get_target_sum, calculate_probability, generate_dice_faces_diagram


def test_get_num_dice():
    # Test valid inputs
    for i in range(1, 7):
        assert get_num_dice(i) == i

    # Test invalid inputs
    with pytest.raises(ValueError):
        get_num_dice(0)
    with pytest.raises(ValueError):
        get_num_dice(7)


def test_get_target_sum():
    # Test valid inputs
    assert get_target_sum(2, 2) == 2
    assert get_target_sum(2, 12) == 12

    # Test invalid inputs
    with pytest.raises(ValueError):
        get_target_sum(2, 1)
    with pytest.raises(ValueError):
        get_target_sum(2, 13)

def test_calculate_probability():
    # Test probabilities for 1 dice
    assert calculate_probability(1, 1) == 1/6
    assert calculate_probability(1, 6) == 1/6

    # Test probabilities for 2 dice
    assert calculate_probability(2, 2) == 1/36
    assert calculate_probability(2, 7) == 6/36
    assert calculate_probability(2, 12) == 1/36

    # Test probabilities for 3 dice
    assert calculate_probability(3, 3) == 1/216
    assert calculate_probability(3, 10) == 27/216
    assert calculate_probability(3, 18) == 1/216


def test_calculate_probability():
    assert calculate_probability(2, 7) == 0.16666666666666666
    assert calculate_probability(1, 3) == 0.16666666666666666
    assert calculate_probability(4, 12) == 0.09645061728395062


def test_generate_dice_faces_diagram():
    num_dice = 1
    dice = [Die() for _ in range(num_dice)]

    # Set specific value for the single die to test the output
    dice[0].value = 3

    expected_output = (
        "~~~~~~~~~ RESULTS ~~~~~~~~~\n"
        "┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘"
    )

    assert generate_dice_faces_diagram(dice) == expected_output


