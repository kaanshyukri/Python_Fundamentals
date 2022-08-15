n = int(input())
pieces = {}
for _ in range(n):
    text = input().split("|")
    piece, composer, key = text[0:]
    pieces[piece] = {"Composer": composer, "Key": key}

command = input()
while command != "Stop":
    command_split = command.split("|")
    if command_split[0] == "Add":
        piece, composer, key = command_split[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command_split[0] == "Remove":
        piece = command_split[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_split[0] == "ChangeKey":
        piece, new_key = command_split[1:]
        if piece in pieces:
            pieces[piece]['Key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for key, value in pieces.items():
    print(f"{key} -> Composer: {value['Composer']}, Key: {value['Key']}")
