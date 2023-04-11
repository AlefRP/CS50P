import inflect

# Calling inflect.engine
p = inflect.engine()

# Main function
def main():
    print("Adieu, adieu, to", get_names())

# Get a list of names from user
def get_names():
    names = []
    while True:
        try:
            name =  input('Name: ').strip()
            names.append(name)
        except EOFError:
            return p.join(names)

# Call main
main()
