import csv
import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv[1]) < 4 or not (sys.argv[1][-4:] == ".csv")
    sys.exit("Not a CSV file")
