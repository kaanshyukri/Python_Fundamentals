events = input().split("|")
energy = 100
coins = 100
condition = True
for event in events:
    types = event.split("-")
    type_of_text = types[0]
    number = int(types[1])

    if type_of_text == "rest":
        if energy >= 100:
            print("You gained 0 energy.")
            print("Current energy: 100.")
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
    elif type_of_text == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            print(f"You bought {type_of_text}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {type_of_text}.")
            condition = False
            break

if condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




