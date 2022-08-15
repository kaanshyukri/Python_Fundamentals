energy = int(input())
distance = input()
win_count = 0

while distance != "End of battle":
    distance = int(distance)
    if energy >= distance:
        energy -= distance
        win_count += 1
        if win_count % 3 == 0:
            energy += win_count
    elif energy < distance:
        print(f"Not enough energy! Game ends with {win_count} won battles and {energy} energy")
        break
    distance = input()

if distance == "End of battle":
    print(f"Won battles: {win_count}. Energy left: {energy}")
