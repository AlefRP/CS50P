# Defining main function
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Cheking validation
def is_valid(s):
    if (len(s) % 2 == 0 and s[round(len(s)/2) - 1].isnumeric()) or (len(s) % 2 != 0 and s[round((len(s) - 1)/2) - 1].isnumeric()):
        return False
    if len(s) < 2:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if len(s) >= 2 and len(s) <= 6:
        for i in range(1):
            if s[i].isnumeric():
                return False
        punctuation_marks = [".", ",", "!", "?", ":", ";", "(", ")", "{", "}", "[", "]", "<", ">", "/", "\\", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "`", "~"]
        for letter in s:
            if letter in punctuation_marks or (letter.isnumeric() and not(s[len(s) - 1].isnumeric())):
                return False
        for letter in s:
            if letter.isnumeric():
                if int(letter) == 0:
                    return False
                break
    else:
        return False
    return True

# Call Main
if __name__ == "__main__":
    main()