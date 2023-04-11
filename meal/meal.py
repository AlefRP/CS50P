# Defining main
def main():
    meal_time = input("What time is it? ")
    meal_time = convert(meal_time)
    if meal_time >= 7 and meal_time <= 8:
        print("breakfast time", end = "")
    elif meal_time >= 12 and meal_time <= 13:
        print("lunch time", end = "")
    elif meal_time >= 18 and meal_time <= 19:
        print("dinner time", end = "")
    else:
        print("")

# Convert time to output
def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours) + minutes/60
    return hours

# Call main
if __name__ == "__main__":
    main()