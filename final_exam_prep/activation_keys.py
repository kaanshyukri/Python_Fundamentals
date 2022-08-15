activation_key = input()

command = input()
while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        type_string, start_index, end_index = command[1:]
        if type_string == "Upper":
            activation_key = activation_key[:int(start_index)]\
             + activation_key[int(start_index):int(end_index)].upper() + activation_key[int(end_index):]
            print(activation_key)
        elif type_string == "Lower":
            activation_key = activation_key[:int(start_index)] \
                             + activation_key[int(start_index):int(end_index)].lower() + activation_key[int(end_index):]
            print(activation_key)
    elif command[0] == "Slice":
        start_index, end_index = command[1:]
        activation_key = activation_key[:int(start_index)] + activation_key[int(end_index):]
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")
