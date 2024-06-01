due = 50
while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin

if due < 0:
    due *= -1
print("Change Owed:", due)
