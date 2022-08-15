n = int(input())
parking = {}
for _ in range(n):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = number
            print(f"{username} registered {number} successfully")
    elif command[0] == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, num in parking.items():
    print(f"{user} => {num}")