from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))
elif len(sys.argv) == 3:
    if not(sys.argv[1] == "-f" or sys.argv[1] == "--font") or not (sys.argv[2] in figlet.getFonts()):
        sys.exit("Error")
    else:
        figlet.setFont(font = sys.argv[2])
else:
    sys.exit("Error")

s = input("Input: ")
print("Output:")
print(figlet.renderText(s))



