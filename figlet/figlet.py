import sys
from pyfiglet import Figlet
import random

# Instantiate figlet and get fonts
figlet = Figlet()
fonts = figlet.getFonts()

# Check for terminal entries, get font and print result
if len(sys.argv) == 1:
    text = input("Input: ")
    select_font = random.choice(fonts)
    figlet.setFont(font=select_font)
    print("Output:", figlet.renderText(text), sep="\n")
elif len(sys.argv) < 4 and sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output:", figlet.renderText(text), sep="\n")
else:
    print(len(sys.argv) < 3)
    sys.exit("Invalid usage")

