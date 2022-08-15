n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    if plant not in plants:
        plants[plant] = {'Rarity': int(rarity), 'Rating': 0, 'Count': 0}
    else:
        plants[plant]['Rarity'] = int(rarity)

command = input()
while command != "Exhibition":
    command_split = command.split()
    text, plant = command_split[0:2]
    if text == "Rate:":
        if plant not in plants:
            print("error")
        else:
            rating = int(command_split[3])
            plants[plant]["Rating"] += rating
            plants[plant]['Count'] += 1
    elif text == "Update:":
        if plant not in plants:
            print("error")
        else:
            new_rarity = int(command_split[3])
            plants[plant]['Rarity'] = new_rarity
    elif text == "Reset:":
        if plant not in plants:
            print("error")
        else:
            plants[plant]['Rating'] = 0
            plants[plant]['Count'] = 0
    command = input()

print('Plants for the exhibition:')
for key, value in plants.items():
    if value['Count'] == 0:
        print(f'- {key}; Rarity: {value["Rarity"]}; Rating: 0.00')
    else:
        print(f'- {key}; Rarity: {value["Rarity"]}; Rating: {value["Rating"]/ value["Count"]:.2f}')
