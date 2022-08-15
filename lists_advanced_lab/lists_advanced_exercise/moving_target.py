numbers = list(map(int, input().split(" ")))

command = input()
while command != "End":
    res = command.split(" ")
    action = res[0]
    index = int(res[1])
    value = int(res[2])
    if action == "Shoot":
        if 0 <= index <= len(numbers):
            numbers[index] -= value
            if numbers[index] <= 0:
                numbers.remove(numbers[index])

    elif action == "Add":
        if 0 > index or index >= len(numbers):
            print("Invalid placement!")
        else:
            numbers.insert(index, value)
    elif action == "Strike":
        if index - value < 0 or index + value > len(numbers):
            print("Strike missed!")
        else:
            del numbers[index:index + value + 1]
            del numbers[index - value:index]
    command = input()

strings = list(map(str, numbers))

print("|".join(strings))
