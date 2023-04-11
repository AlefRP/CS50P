# Get fraction from user
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge_value = gauge(percentage)
    print(gauge_value)


# Fraction Calculator
def convert(fraction):
    numerator, denominator =  map(int, fraction.strip().split("/"))
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator > denominator:
        raise ValueError
    else:
        return round(numerator/denominator * 100)


# Gauge Function
def gauge(percentage):
    if percentage == 0 or percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

# Call main
if __name__ == "__main__":
    main()
