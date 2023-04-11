# Get camel case from user
def main():
    camel_case = input("camelCase: ")
    print(converter(camel_case))

# Loop changes upper to lower and add "_" before
def converter(text):
    result = ""
    for letter in text:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    return result

# Call main
main()
