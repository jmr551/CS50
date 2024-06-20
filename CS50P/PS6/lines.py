import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv[1][-3:]) < 3 or not(sys.argv[1][-3:] == ".py"):
    sys.exit("Not a Python file")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

