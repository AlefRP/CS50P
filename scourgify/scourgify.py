import sys
import csv
import os

# check number of command-line arguments
if len(sys.argv) != 3 and len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

# check if first CSV file exists
if not os.path.isfile(sys.argv[1]):
    sys.exit("Could not read " + sys.argv[1])

# read the CSV file
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# clean the data
new_data = []
for row in data:
    last, first = row['name'].split(',')
    new_row = {
        'first': first.strip(),
        'last': last.strip(),
        'house': row['house'].strip()
    }
    new_data.append(new_row)

# write the cleaned data to a new CSV file
with open(sys.argv[2], 'w', newline='') as csvfile:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_data:
        writer.writerow(row)