# Main Function
def main():
    print(taq_calculator())

# Taq Calculator
def taq_calculator():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_price = 0
    while True:
        try:
            order = input("Item: ").lower().title()
            if order in menu:
                total_price += menu[order]
                print(f"${total_price:.2f}")
        except KeyError:
            pass
        except EOFError:
            break
# Call Main
main()
