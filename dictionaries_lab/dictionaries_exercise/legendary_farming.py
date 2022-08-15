command = input().split(" ")
my_dict = {}
premium_dict = {"shards": 0, "fragments": 0, "motes": 0}
condition = False
name = ""

while command:
    for _ in range(int(len(command)/2)):
        if command[1].lower() == "fragments" or command[1].lower() == "motes" or command[1].lower() == "shards":
            premium_dict[command[1].lower()] += int(command[0])
            if premium_dict[command[1].lower()] >= 250:
                condition = True
                break
            del command[0:2]
        else:
            if command[1].lower() not in my_dict:
                my_dict[command[1].lower()] = 0
            my_dict[command[1].lower()] += int(command[0])
            del command[0:2]
        if condition:
            break
    if condition:
        break
    command = input().split()


for k, v in premium_dict.items():
    if v >= 250:
        premium_dict[k] -= 250
        if k == "shards":
            name = "Shadowmourne"
            break
        elif k == "fragments":
            name = "Valanyr"
            break
        elif k == "motes":
            name = "Dragonwrath"
            break
print(f"{name} obtained!")


for item, number in premium_dict.items():
    print(f"{item}: {number}")

for junk, num in my_dict.items():
    print(f"{junk}: {num}")
