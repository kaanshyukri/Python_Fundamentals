text = input()
new_text = ""
for t in text:
    res = ord(t) + 3
    new_text += chr(res)
print(new_text)
