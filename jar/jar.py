class Jar:
    def __init__(self, capacity=12):
        # Check if the capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        # Return a string representation of the cookies in the jar
        return "\U0001F36A" * self.cookies

    def deposit(self, n):
        # Deposit n cookies into the jar, checking if it exceeds capacity
        if n + self.cookies > self.capacity:
            raise ValueError(f"Jar capacity is {self.capacity}")
        self.cookies += n

    def withdraw(self, n):
        # Withdraw n cookies from the jar, checking if there are enough cookies
        if n > self.cookies:
            raise ValueError(f"Jar has only {self.cookies} cookies")
        self.cookies -= n

    @property
    def size(self):
        # Return the current number of cookies in the jar
        return self.cookies

    @property
    def capacity(self):
        # Return the maximum capacity of the jar
        return self.capacity

def main():
    # Get user input for the jar capacity and the number of cookies to insert
    capacity = int(input("Capacity: "))
    quantity = int(input("How many do you wanna insert? "))

    # Create a jar object and deposit the specified number of cookies
    jar = Jar(capacity)
    jar.deposit(quantity)

    # Display the jar's capacity and current size
    print(f"Capacity: {jar.capacity}")
    print(f"Current Size: {jar.size}")

    # Get user input for the number of cookies to withdraw
    withdraw = int(input("Withdraw: "))

    # Withdraw the specified number of cookies and display the updated jar
    jar.withdraw(withdraw)
    print(jar)

if __name__ == '__main__':
    main()