import sys
import os
import re

# Check if the user has provided exactly one command-line argument
if len(sys.argv) != 2 and len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

# Check if the file specified by the user exists and ends with '.py'
filename = sys.argv[1]
if not os.path.isfile(filename):
    sys.exit('File does not exist')
if not filename.endswith('.py'):
    sys.exit('Not a Python file')

# Open the file and read its contents line by line
with open(filename, 'r') as file:
    code_lines = 0
    for line in file:
        # Check if the line is blank or a comment
        if not re.match(r'^\s*(#|$)', line):
            code_lines += 1

# Print the count of lines of code
print(code_lines)
