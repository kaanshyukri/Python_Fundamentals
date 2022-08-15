command = input()
chat_list = []
while command != "end":
    res = command.split()
    action = res[0]
    if action == "Chat":
        message = res[1]
        chat_list.append(message)
    elif action == "Delete":
        message = res[1]
        if message in chat_list:
            chat_list.remove(message)
    elif action == "Edit":
        message = res[1]
        version = res[2]
        if message in chat_list:
            for i in range(len(chat_list)):
                if chat_list[i] == message:
                    chat_list[i] = version
    elif action == "Pin":
        message = res[1]
        if message in chat_list:
            chat_list.remove(message)
            chat_list.append(message)
    elif action == "Spam":
        message = res[1::]
        for mes in message:
            chat_list.append(mes)
    command = input()

print("\n".join(chat_list))
