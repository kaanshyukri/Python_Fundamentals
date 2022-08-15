import re

text = input()
find_numbers = r"\d"
numbers = re.findall(find_numbers, text)
threshold = 1
for n in numbers:
    threshold *= int(n)
print(f"Cool threshold: {threshold}")

find_emojis = r"(::|\*\*)[A-Z][a-z]{2,}\1"
emojis = re.finditer(find_emojis, text)
emoji_list = []
for e in emojis:
    emoji_list.append(e.group())

valid_emojis = []
for emoji in emoji_list:
    count = 0
    text_emoji = emoji.replace(emoji[0], "")
    for letter in text_emoji:
        count += ord(letter)
    if count >= threshold:
        valid_emojis.append(emoji)

print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for valid in valid_emojis:
    print(valid)
