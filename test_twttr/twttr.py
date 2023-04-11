# Main Function
def main():
    sentence = input("Input: ")
    print(shorten(sentence))

# Short converter
def shorten(word):
    result = ""
    for letter in word:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            result += letter
    return result

# Call main
if __name__ == "__main__":
    main()