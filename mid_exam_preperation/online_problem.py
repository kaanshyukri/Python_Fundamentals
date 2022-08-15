rooms = input().split("|")
health = 100
condition = False
count = 0
bitcoins = 0
for r in rooms:
    count += 1
    res = r.split()
    room = res[0]
    number = int(res[1])
    if room == "potion":
        health += number
        if health > 100:
            calc = number - (health - 100)
            health = 100
            print(f"You healed for {calc} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
    elif room == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            print(f"You died! Killed by {room}.")
            print(f"Best room: {count}")
            condition = True
            break
        else:
            print(f"You slayed {room}.")

if not condition:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
