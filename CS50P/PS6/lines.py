import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv[1][-3:]) < 3 or not(sys.argv[1][-3:] == ".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

count = 0
with open(sys.argv[1]) as file:
    for line in file:
        line=line.strip()
        if len(line) > 0 and line[0] != "#":
            count += 1

print(count)
