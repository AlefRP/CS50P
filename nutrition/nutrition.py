# Get user input
fruit_input = input("Item: ").lower().strip()

# Raw Fruits Data base
raw_fruits = [
    {"name": "apple", "calories": 130},
    {"name": "avocado", "calories": 50},
    {"name": "sweet cherries", "calories": 100},
    {"name": "kiwifruit", "calories": 90},
    {"name": "pear", "calories": 100}
]

# Print Calories
for fruit in raw_fruits:
    if fruit["name"] == fruit_input:
        print("Calories:", fruit["calories"])