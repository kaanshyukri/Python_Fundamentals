letters = input().split(", ")
ascii_letters = {}

for _ in range(len(letters)):
    ascii_letters = {l:ord(l) for l in letters}

print(ascii_letters)
