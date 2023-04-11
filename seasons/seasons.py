from datetime import date
import re
import sys
import inflect

class Person:
    def __init__(self, dob):
        self.dob = dob

    def age_in_minutes(self):
        return calculate_age_in_minutes(self.dob)

    def age_in_words(self):
        age_in_minutes = self.age_in_minutes()
        return number_to_words(age_in_minutes)

# Function to calculate age in minutes
def calculate_age_in_minutes(dob):
    age_in_seconds = (date.today() - dob).total_seconds()
    age_in_minutes = age_in_seconds // 60
    return int(age_in_minutes)

# Function to convert a number to words
def number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number).capitalize()
    return words.replace(" and ", " ")

# Main function to run the program
def main():
    # Prompt user for date of birth input
    dob_input = input("Date of Birth: ")

    # Check if the input date is valid and extract the date object
    validation, dob = date_is_valid(dob_input)

    if validation:
        # Create a Person object with the input date
        person = Person(dob)

        # Print the age in minutes as English words
        print(person.age_in_words(), "minutes")
    else:
        # Exit the program with an error message if the date is invalid
        sys.exit("Invalid date")

# Function to validate the input date format and return the date object
def date_is_valid(date_str):
    # Check if the input string matches the required date format (YYYY-MM-DD)
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    if not pattern.match(date_str):
        return False, None

    try:
        # Convert the input string to a date object
        year, month, day = (int(x) for x in date_str.split("-"))
        dob = date(year, month, day)
        return True, dob
    except ValueError:
        return False, None

# Run the main function
if __name__ == "__main__":
    main()