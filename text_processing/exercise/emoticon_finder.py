text = input()
n = 0
for t in text:
    n += 1
    if ":" == t:
     print(f"{t}{text[n]}")
