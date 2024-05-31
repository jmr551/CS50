x, y, z = input("Expression: ").strip().split()

x = float(x)
z = float(z)

if y == "+":
    print (f"{x + z}")
elif y == "-":
    print (x - z)
elif y == "*":
    print (x * z)
else:
    print (x / z)


