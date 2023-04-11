# Get coin from user
def main():
    update_amount()

# Update coin amount
def update_amount():
    amount = 50
    owed = 0
    print("Amount Due:", amount)
    while True:
        coin = int(input("Insert Coin: ").strip())
        if coin in (5, 10, 25):
            amount -= coin
        if amount > 0:
            print("Amount Due:", amount)
            continue
        else:
            owed += amount * -1
            amount = 0
            print("Change Owed:", owed, end="\n")
            break

# Call main
main()
