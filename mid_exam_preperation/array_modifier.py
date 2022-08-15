array = list(map(int, input().split()))
command = input()

while command != "end":
    if command == "decrease":
        for a in range(len(array)):
            array[a] -= 1
        command = input()
        continue
    res = command.split()
    action = res[0]
    index_one = int(res[1])
    index_two = int(res[2])
    if action == "swap":
        array[index_one], array[index_two] = array[index_two], array[index_one]

    elif action == "multiply":
        multiply = array[index_one] * array[index_two]
        array.pop(index_one)
        array.insert(index_one, multiply)

    command = input()

str_array = [str(x) for x in array]
print(", ".join(str_array))
