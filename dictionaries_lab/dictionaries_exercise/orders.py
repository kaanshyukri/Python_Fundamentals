command = input()
products = {}

while command != "buy":
    command = command.split()
    product_name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product_name not in products:
        products[product_name] = {}
        products[product_name]['quantity'] = quantity
    elif product_name in products:
        products[product_name]['quantity'] += quantity
    products[product_name]['price'] = price
    command = input()
price = 1

for key, value in products.items():
    for value in value.values():
        price *= value
    print(f"{key} -> {price:.2f}")
    price = 1

