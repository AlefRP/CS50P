#Main Function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Convert dollar to float
def dollars_to_float(d):
    d_value = float(d.removeprefix("$"))
    return d_value

#Convert percentage to float
def percent_to_float(p):
    p_value = float(p.removesuffix("%"))/100
    return p_value

#Call Main()
main()