import re
text = input()
res = re.split('(\d+)', text)
del res[-1]
symbol = []
new_text = ""
for index in range(0, len(res), 2):
    first = res[index].upper()
    second = int(res[index + 1])
    new_text += first * second
    for f in first:
        if f not in symbol:
            symbol.append(f)
print(f"Unique symbols used: {len(symbol)}")
print(new_text)
