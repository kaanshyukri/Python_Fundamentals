command = input()
company = {}
while command != "End":
    command = command.split(" -> ")
    name = command[0]
    Id = command[1]
    if name not in company:
        company[name] = []
        company[name].append(Id)
    elif name in company:
        if Id not in company[name]:
            company[name].append(Id)
    command = input()

for key, values in company.items():
    print(key)
    for v in values:
        print(f"-- {v}")
