#Get the user input
number = input("Greeting: ").strip()

#Verify answer
if number.startswith("Hello"):
    print("\u0024", "0", sep = "")
elif number.startswith("H"):
    print("\u0024", "20", sep = "")
else:
    print("\u0024", "100", sep = "")