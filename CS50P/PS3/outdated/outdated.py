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

    # formato mes/dia/anho
    if "/" in fecha:
        try:
            m, d, a = list(map(int, fecha.split("/")))
        except ValueError:
            continue
    # formato Setiembre 5, 1968
    else:
        if m in months:
            months
