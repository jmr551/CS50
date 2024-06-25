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
            l, f = line["name"].split(",")
            d["first"], d["last"] = (f.strip(), l.strip())
            d["house"] = line["house"]
            new.append(d)
            print(d)
except FileNotFoundError:
    sys.exit("Could not read "+ sys.argv[1])

with open(sys.argv[2],"w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for d in new:
        writer.writerow(d)
