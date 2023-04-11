import sys
import os
from tabulate import tabulate

# Check if the command-line is provided
if len(sys.argv) != 2 and len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

# Check if the file specified by the user exists
csv_file = sys.argv[1]
if not os.path.isfile(csv_file):
    sys.exit('File does not exist')
if not csv_file.endswith('.csv'):
    sys.exit('Not a CSV file')

# Read the CSV file specified in the comand line
with open(csv_file, 'r') as file:
    # Read the lines of the CSV file
    lines = file.readlines()

# Remove the newline character from each line and split by comma
data = [line.strip().split(',') for line in lines]

# Use the tabulate package to format the data as ASCII art
table = tabulate(data, headers='firstrow', tablefmt='grid')

# Print the formatted table to the console
print(table)
