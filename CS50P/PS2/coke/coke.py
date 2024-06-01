due = 50
while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert coin: "))
    due -= coin

if due < 0:
    due *= -1
print("Change Owed:", due)
