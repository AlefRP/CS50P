# Main Function
def main():
    sentence = input("Input: ")
    print(short_converter(sentence))

# Short converter
def short_converter(text):
    result = ""
    for letter in text:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            result += letter
    return result

# Call main
main()
