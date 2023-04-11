# Main function
def main():
    #Get the user input
    greeting = input("Greeting: ").strip()
    value = value(greeting)
    print(f"\u0024{value}", sep = "")

# Check value and print output
def value(greeting):
    #Verify answer
    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100


# Call main
if __name__ == "__main__":
    main()