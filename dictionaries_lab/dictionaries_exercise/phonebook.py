people_phone = input()
phonebook = {}
while "-" in people_phone:
    res = people_phone.split("-")
    name = res[0]
    number = res[1]
    phonebook[name] = number
    people_phone = input()

people_phone = int(people_phone)

for _ in range(people_phone):
    name = input()
    if name in phonebook:
        for value in phonebook:
            if name == value:
                print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
