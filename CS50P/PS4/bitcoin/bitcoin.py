import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    requests.get()
#except requests.RequestException:
#    ...
