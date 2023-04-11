from um import count

def test_count():
    assert count("I am um not sure um") == 2
    assert count("um, I am not sure") == 1
    assert count("I am not sure, um") == 1
    assert count("Um, I am not sure, um") == 2
    assert count("This is a hummus recipe") == 0
    assert count("I am not sure") == 0
