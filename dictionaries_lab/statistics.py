command = input()
my_dict = {}

while command != "statistics":
    res = command.split(":")
    product = res[0]
    quantity = int(res[1])
    if product not in my_dict:
        my_dict[product] = 0

    my_dict[product] += quantity
    command = input()

print("Products in stock:")
for (key, value) in my_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")


