neighbourhood = list(map(int, input().split("@")))
command = input()
count = 0
while command != "Love!":
    action = command.split(" ")
    number = int(action[1])
    count += number
    if count + 1 > len(neighbourhood):
        count = 0
    if neighbourhood[count] == 0:
        print(f"Place {count} already had Valentine's day.")
        command = input()
        continue
    if count <= len(neighbourhood):
        neighbourhood[count] -= 2
        if neighbourhood[count] <= 0:
            neighbourhood[count] = 0
            print(f"Place {count} has Valentine's day.")
    command = input()

filtered = list(filter(lambda x: x > 0, neighbourhood))
print(f"Cupid's last position was {count}.")
if len(filtered) > 0:
    print(f"Cupid has failed {len(filtered)} places.")
else:
    print(f"Mission was successful.")
