gr = input("Greeting: ").strip().lower()

if gr[:5] == "hello":
    print("$0")
elif gr[0] == 'h':
    print("$20")
else:
    print("$100")
