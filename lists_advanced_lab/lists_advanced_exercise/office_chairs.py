number = int(input())
count = 0
needed = 0
room = 0
condition = True
for i in range(number):
    info = input().split(" ")
    chair = info[0]
    visitors = int(info[1])
    room += 1
    if len(chair) < visitors:
        needed = visitors - len(chair)
        print(f"{needed} more chairs needed in room {room}")
        condition = False
    elif len(chair) > visitors:
        count += (len(chair) - visitors)

if condition:
    print(f"Game On, {count} free chairs left")




