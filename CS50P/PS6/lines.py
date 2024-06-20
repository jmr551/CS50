import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if  argv[1][-3:]:
    sys.exit("Not a Python file")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

