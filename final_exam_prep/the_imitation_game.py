message = input()
encrypted = input()

while encrypted != "Decode":
    encrypted_split = encrypted.split("|")
    if encrypted_split[0] == "Move":
        number_of_letters = int(encrypted_split[1])
        message = message[number_of_letters:] + message[0:number_of_letters]
    elif encrypted_split[0] == "Insert":
        index, value = (encrypted_split[1:])
        message = message[:int(index)] + value + message[int(index):]
    elif encrypted_split[0] == "ChangeAll":
        substring, replacement = encrypted_split[1:]
        message = message.replace(substring, replacement)
    encrypted = input()

print(f"The decrypted message is: {message}")
