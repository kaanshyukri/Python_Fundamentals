command = input().split()
my_dict = {}

for i in range(0, len(command), 2):
    my_dict[command[i]] = int(command[i + 1])

print(my_dict)