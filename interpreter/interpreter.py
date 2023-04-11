#Get user's input
def main():
    operation = input("Expression: ").strip()
    print(float(calculator(operation)))

#Fuction to calculate
def calculator(calc):
    x, y, z = calc.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z

#Call main function
main()
