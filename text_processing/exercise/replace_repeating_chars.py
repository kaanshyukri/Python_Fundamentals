text = input()
last_letter = ""
new_text = ""
for letter in text:
    if letter != last_letter:
        new_text += letter
        last_letter = letter
print(new_text)
