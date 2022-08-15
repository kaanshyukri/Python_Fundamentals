coffee_order = input().split()
count = int(input())

for _ in range(count):
    command = input()
    if command == "Reverse":
        coffee_order.reverse()
        continue
    res = command.split()
    action = res[0]
    index = res[1]
    if action == "Include":
        coffee_order.append(index)
    elif action == "Remove":
        second_index = int(res[2])
        if index == "first":
            coffee_order = coffee_order[second_index::]
        elif index == "last":
            coffee_order = coffee_order[:-second_index]
    elif action == "Prefer":
        index = int(index)
        second_index = int(res[2])
        if 0 <= index < len(coffee_order) and 0 <= second_index < len(coffee_order):
            coffee_order[index], coffee_order[second_index] = coffee_order[second_index], coffee_order[index]

coffee_order = " ".join(coffee_order)
print(f"Coffees:\n"
      f"{coffee_order}")

