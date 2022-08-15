groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    res = command.split()
    action = res[0]
    item = res[1]
    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        new_item = res[2]
        if item in groceries:
            for product in range(len(groceries)):
                if groceries[product] == item:
                    groceries[product] = new_item
    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()

print(", ".join(groceries))
