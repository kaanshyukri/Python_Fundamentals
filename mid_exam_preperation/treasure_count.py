loots = input().split("|")
command = input()
new_list = []
while command != "Yohoho!":
    res = command.split(" ")
    action = res[0]
    if action == "Loot":
        items = res[1:]
        for item in items:
            if item not in loots:
                loots.insert(0, item)
    elif action == "Drop":
        index = int(res[1])
        if 0 <= abs(index) <= len(loots):
            removing = loots.pop(index)
            loots.append(removing)
    elif action == "Steal":
        number = int(res[1])
        removed_items = loots[-number:]
        print(", ".join(removed_items))
        loots = loots[:-number]
    command = input()

if len(new_list) > 0:
    new_list.reverse()
    print(", ".join(new_list))
count = 0
for y in loots:
    count += len(y)

if len(loots) > 0:
    print(f"Average treasure gain: {float(count / len(loots)):.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")



