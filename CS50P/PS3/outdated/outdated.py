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
    fecha = input("Date: ").title()

    # formato mes/dia/anho
    if "/" in fecha:
        try:
            m, d, a = list(map(int, fecha.split("/")))
        except ValueError:
            continue
    # formato Setiembre 5, 1968
    else:
        try:
            m, d, a = fecha.split()
            d = int(d)
            a = int(a)
        except ValueError:
            continue
        if m in months:
            m = months.index(m) + 1
            print (m)
        else:
            continue
        