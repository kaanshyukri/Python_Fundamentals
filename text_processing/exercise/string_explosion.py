text = input()
new_text = ""
strength = 0

for t in range(len(text)):
    if text[t] != ">" and strength > 0:
        strength -= 1

    elif text[t] == ">":
        strength += int(text[t+1])
        new_text += text[t]
    else:
        new_text += text[t]
print(new_text)
