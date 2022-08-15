word = input()
char = {}
for s in word:
    if s not in char and s != " ":
        char[s] = 1
    elif s in char:
        char[s] += 1

for key, value in char.items():
    print(f"{key} -> {value}")
