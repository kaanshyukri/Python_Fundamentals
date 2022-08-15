destination = input()
command = input()

while command != "Travel":
    command_split = command.split(":")
    if command_split[0] == "Add Stop":
        index, string = command_split[1:]
        index = int(index)
        if index < len(destination):
            destination = destination[:index] + string + destination[index:]
        print(destination)
    elif command_split[0] == "Remove Stop":
        start_index, end_index = command_split[1:]
        if 0 <= int(start_index) and int(end_index) < len(destination):
            destination = destination[:int(start_index)] + destination[int(end_index)+1:]
        print(destination)
    elif command_split[0] == "Switch":
        old_string, new_string = command_split[1:]
        if old_string in destination:
            destination = destination.replace(old_string, new_string)
        print(destination)
    command = input()

print(f"Ready for world tour! Planned stops: {destination}")
