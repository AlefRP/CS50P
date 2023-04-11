# Main Function
def main():
    itens = grocery_list()
    for item in sorted(itens):
        print(itens[item], item)

# Grocery list
def grocery_list():
    itens = {}
    total = 0
    while True:
        try:
            item = input().upper()
            if item == "":
                break
            elif item in itens:
                total += 1
            else:
                total = 1  # set total back to 1 for new items
            itens[item] = total
        except KeyError:
            break
        except EOFError:
            return itens

# Call Main
main()
