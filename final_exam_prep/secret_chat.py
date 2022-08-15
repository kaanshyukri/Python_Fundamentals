text = input()
message = input()

while message != "Reveal":
    message_split = message.split(":|:")
    if message_split[0] == "InsertSpace":
        index = int(message_split[1])
        text = text[0:index] + " " + text[index:]
        print(text)
    elif message_split[0] == "Reverse":
        substring = message_split[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            substring = substring[::-1]
            text = text + substring
            print(text)
        else:
            print("error")
    elif message_split[0] == "ChangeAll":
        substring, replacement = message_split[1:]
        text = text.replace(substring, replacement)
        print(text)
    message = input()

print(f"You have a new text message: {text}")
