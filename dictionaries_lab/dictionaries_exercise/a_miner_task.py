metals = {}
while True:
    name = input()
    if name == "stop":
        for k, v in metals.items():
            print(f"{k} -> {v}")
        break
    number = int(input())
    if name not in metals:
        metals[name] = number
    elif name in metals:
        metals[name] += number
