pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
health = int(input())
command = input()
condition = False
second_condition = False

while command != "Retire":
    res = command.split()
    action = res[0]
    if action == "Status":
        total = 0
        low_health = health * 0.20
        for section in pirate_ship:
            if section < low_health:
                total += 1
        print(f"{total} sections need repair.")
        command = input()
        continue
    index = int(res[1])
    if action == "Fire":
        if 0 <= index < len(war_ship):
            damage = int(res[2])
            war_ship[index] -= damage
            second_condition = True
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                condition = True
                break
    elif action == "Defend":
        second_index = int(res[2])
        damage = int(res[3])
        if 0 <= index < len(pirate_ship) and 0 <= second_index < len(pirate_ship):
            second_condition = True
            for i in range(index, second_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    condition = True
                    break
    elif action == "Repair":
        if 0 <= index < len(pirate_ship):
            repair = int(res[2])
            pirate_ship[index] += repair
            if pirate_ship[index] > health:
                pirate_ship[index] = health
    if condition:
        break
    command = input()

if second_condition and not condition:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(war_ship)}")
