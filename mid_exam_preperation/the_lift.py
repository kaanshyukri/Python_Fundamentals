people_waiting = int(input())
wagons = list(map(int, input().split()))
wagon_list = []
for wagon in wagons:
    if people_waiting == 0:
        wagon_list.append(wagon)
        continue
    if wagon == 4:
        wagon_list.append(wagon)
        continue
    elif wagon == 3:
        wagon += 1
        people_waiting -= 1
        wagon_list.append(wagon)
    elif wagon == 2:
        wagon += 2
        people_waiting -= 2
        wagon_list.append(wagon)
    elif wagon == 1:
        if people_waiting < 4:
            wagon += people_waiting
            people_waiting -= people_waiting
            wagon_list.append(wagon)
            continue
        wagon += 3
        people_waiting -= 3
        wagon_list.append(wagon)
    elif wagon == 0:
        if people_waiting < 4:
            wagon_list.append(people_waiting)
            people_waiting -= people_waiting
            continue
        wagon += 4
        people_waiting -= 4
        wagon_list.append(wagon)

condition = False
wagon_list = [str(x) for x in wagon_list]
without = " ".join(wagon_list)
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n"
          f"{without}")
elif people_waiting == 0:
    if not condition:
        for space in wagon_list:
            if int(space) < 4:
                condition = True
        if condition:
            print(f"The lift has empty spots!\n"
                  f"{without}")
        else:
            print(" ".join(wagon_list))
