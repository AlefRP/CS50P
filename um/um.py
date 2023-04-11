import re

def main():
    # Get user input and store it in the variable 'text'
    text = input("Input: ")
    # Call the 'count' function and print the result
    print(count(text))

def count(s):
    # Use regex to find all occurrences of the word "um" in the input string
    # The regex pattern '\b(?:um)\b' matches the exact word "um" surrounded by word boundaries
    um_count = len(re.findall(r'\b(?:um)\b', s.lower()))
    # Return the count of "um" occurrences
    return um_count

if __name__ == "__main__":
    main()