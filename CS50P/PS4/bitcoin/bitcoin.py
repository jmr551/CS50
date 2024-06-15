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
    respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respuesta = respuesta.json()
except requests.RequestException:
    sys.exit("Error al realizar el request.")
else:
    respuesta = respuesta["bpi"]["USD"]["rate"].split(",")
    amount = 1000*float(respuesta[0]) + float(respuesta[1]) * n
    print(f"${amount:,.4f}")
