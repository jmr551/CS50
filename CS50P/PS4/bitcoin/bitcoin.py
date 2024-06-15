import json
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
    respuesta = json.loads(requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").content)
except requests.RequestException:
    sys.exit("Error al realizar el request.")
else:
    print(respuesta.keys())
