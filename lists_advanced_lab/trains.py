wagons = int(input())
wagon_list = [0] * wagons
command = input()

while command != "End":
    info = command.split(" ")
    wagon = info[0]
    number = int(info[1])
    if wagon == "add":
        wagon_list[-1] += number
    elif wagon == "insert":
        second_num = int(info[2])
        wagon_list[number] += second_num
    elif wagon == "leave":
        second_num = int(info[2])
        wagon_list[number] -= second_num

    command = input()

print(wagon_list)
