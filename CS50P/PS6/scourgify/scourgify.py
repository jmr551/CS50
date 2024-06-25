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
            d["last"], d["first"] = line["name"].split(",")
            d["first"] = d["first"].strip()
            d["last"] = d["last"].strip()
            d["house"] = line["house"]
            new.append(d)
            print(d)
except FileNotFoundError:
    sys.exit("Could not read "+ sys.argv[1])

with open(sys.argv[2],"w") as file:
    for line in new:
        print(line)
