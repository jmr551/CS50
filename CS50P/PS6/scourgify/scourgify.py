import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        new = []
        for line in reader:
            d = {}
            d["first"] =
            d["last"] =
            d["house"] =

except FileNotFoundError:
    sys.exit("Could not read "+ sys.argv[1])

