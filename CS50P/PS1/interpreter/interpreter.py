x, y, z = input("Expression: ").strip().split()

x = float(x)
z = float(z)

if y == "+":
    print (f"{(x + z):.1f}")
elif y == "-":
    print (f"{(x - z):.1f}")
elif y == "*":
    print (f"{(x * z):.1f}")
else:
    print (f"{(x / z):.1f}")


