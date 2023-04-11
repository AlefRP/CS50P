import re

# Main function
def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Check if the input matches the expected format
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
            raise ValueError("Invalid input format")

    if match:
        group2 = match.group(2) if match.group(2) else 0
        group5 = match.group(5) if match.group(5) else 0

    if int(group2) >= 60 or int(group5) >= 60:
        raise ValueError("Invalid input format")


    # Extract the two times from the match object
    hour1 = int(match.group(1))
    minute1 = int(group2)
    am_pm1 = match.group(3)
    hour2 = int(match.group(4))
    minute2 = int(group5)
    am_pm2 = match.group(6)


    # Convert the hours to 24-hour format
    if hour1 == 12:
        hour1 = 0
    if am_pm1 == "PM":
        hour1 += 12
    if hour2 == 12:
        hour2 = 0
    if am_pm2 == "PM":
        hour2 += 12

    # Convert hours and minutes to strings with leading zeros
    hour1_str = str(hour1).zfill(2)
    minute1_str = str(minute1).zfill(2)
    hour2_str = str(hour2).zfill(2)
    minute2_str = str(minute2).zfill(2)

    # Return the times in 24-hour format
    return f"{hour1_str}:{minute1_str} to {hour2_str}:{minute2_str}"


# Call main
if __name__ == "__main__":
    main()