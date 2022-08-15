max_capacity = int(input())
messages = {}

command = input()
while command != "Statistics":
    command = command.split("=")
    if command[0] == "Add":
        username, sent, received = command[1:]
        if username not in messages:
            messages[username] = {'sent': int(sent), 'received': int(received)}
    elif command[0] == "Message":
        sender, receiver = command[1:]
        if sender in messages and receiver in messages:
            messages[sender]['sent'] += 1
            messages[receiver]['received'] += 1
            if messages[sender]['sent'] + messages[sender]['received'] >= max_capacity:
                del messages[sender]
                print(f"{sender} reached the capacity!")
            if messages[receiver]['received'] + messages[receiver]['sent'] >= max_capacity:
                del messages[receiver]
                print(f"{receiver} reached the capacity!")
    elif command[0] == "Empty":
        username = command[1]
        if username == "All":
            messages.clear()
        else:
            del messages[username]
    command = input()

print(f"Users count: {len(messages)}")
for key, value in messages.items():
    print(f"{key} - {value['sent'] + value['received']}")
