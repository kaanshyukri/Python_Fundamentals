text = input()
cities = {}
while text != "Sail":
    text = text.split("||")
    city, population, gold = text[0:]
    if city not in cities:
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += int(population)
    cities[city]['gold'] += int(gold)
    text = input()

command = input()
while command != "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        town, people, gold = command[1:]
        cities[town]['population'] -= int(people)
        cities[town]['gold'] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif command[0] == "Prosper":
        town, gold = command[1:]
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
