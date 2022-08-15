product = input()
amount = int(input())


def order(drink, count):
    result = 0
    if drink == "coffee":
        result = count * 1.5
    elif drink == "water":
        result = count * 1
    elif drink == "coke":
        result = count * 1.4
    elif drink == "snacks":
        result = count * 2


price = order(product, amount)
print(f"{price:.2f}")

    