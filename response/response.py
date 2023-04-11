# Import the 'validators' library
import validators

# Define the main function
def main():
    # Prompt the user for an email address
    email = input("What's your email address? ")

    # Check if the input is a syntactically valid email address using 'validators.email()'
    if validators.email(email):
        # If the email is valid, print "Valid"
        print("Valid")
    else:
        # If the email is not valid, print "Invalid"
        print("Invalid")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
