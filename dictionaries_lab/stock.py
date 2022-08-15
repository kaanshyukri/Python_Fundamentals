command = input().split()
my_dict = {}

for i in range(0, len(command), 2):
    my_dict[command[i]] = int(command[i + 1])

food = input().split()

for f in food:
    if f not in  my_dict:
        print(f"Sorry, we don't have {f}")
    else:
        print(f"We have {my_dict[f]} of {f} left")
