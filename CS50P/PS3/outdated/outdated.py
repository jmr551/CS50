months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    fecha = input("Date: ")

    # mes/dia/anho
    if "/" in fecha:
        try:
            m, d, a = fecha.split("/")
            m = int(m)
            d = int(d)
            a = int(a)
        except ValueError:
            continue
