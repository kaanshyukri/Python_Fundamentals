info = input().split("|")
budget = int(input())
profit = 0
adding = []
second_list = []
for types in info:
    current_type = types.split("->")
    type_of = current_type[0]
    price = float(current_type[1])
    if budget < price:
        continue
    if type_of == "Clothes":
        if price <= 50:
            budget -= price
            new_price = price + (price * 0.40)
            profit += price * 0.40
            adding.append(new_price)
            second_list.append(f"{new_price:.2f}")
    elif type_of == "Shoes":
        if price <= 35:
            budget -= price
            new_price = price + (price * 0.40)
            profit += price * 0.40
            adding.append(new_price)
            second_list.append(f"{new_price:.2f}")
    elif type_of == "Accessories":
        if price <= 20.50:
            budget -= price
            new_price = price + (price * 0.40)
            profit += price * 0.40
            adding.append(new_price)
            second_list.append(f"{new_price:.2f}")


print("  ".join(second_list))
print(f"Profit: {profit:.2f}")

total_sum = sum(adding) + budget
if total_sum >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')


