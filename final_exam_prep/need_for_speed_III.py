n = int(input())
cars = {}

for _ in range(n):
    car, distance, fuel = input().split("|")
    cars[car] = {'distance': int(distance), 'fuel': int(fuel)}

text = input()
while text != "Stop":
    command = text.split(" : ")
    if command[0] == "Drive":
        car, distance, fuel = command[1:]
        distance = int(distance)
        fuel = int(fuel)
        if cars[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['distance'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['distance'] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car, fuel = command[1:]
        fuel = int(fuel)
        if cars[car]['fuel'] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car, kilometers = command[1:]
        kilometers = int(kilometers)
        cars[car]['distance'] -= kilometers
        if cars[car]['distance'] < 10000:
            cars[car]['distance'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    text = input()

for key, value in cars.items():
    print(f"{key} -> Mileage: {value['distance']} kms, Fuel in the tank: {value['fuel']} lt.")
