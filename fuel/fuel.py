# Get fraction from user
def main():
    print(fraction_calculator())

# Fraction Calculator
def fraction_calculator():
    while True:
        try:
            numerator, denominator =  map(int, input("Fraction: ").strip().split("/"))
            result = numerator/denominator
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if result == 0 or result <= 0.01:
                return "E"
            elif result == 1 or (result >= 0.99 and result <= 1):
                return "F"
            elif result > 1:
                pass
            else:
                return str(round(result * 100)) + "%"
# Call main
main()
