collecting_items = input().split(", ")
commands = input()

while commands != "Craft!":
    res = commands.split(" - ")
    action = res[0]
    item = res[1]
    if action == "Collect" and item not in collecting_items:
        collecting_items.append(item)
    elif action == "Drop" and item in collecting_items:
        collecting_items.remove(item)
    elif action == "Combine Items":
        combined = item.split(":")
        old = combined[0]
        new = combined[1]
        if old in collecting_items:
            old_index = collecting_items.index(old)
            collecting_items.insert(old_index + 1, new)
    elif action == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)
    commands = input()

print(", ".join(collecting_items))



