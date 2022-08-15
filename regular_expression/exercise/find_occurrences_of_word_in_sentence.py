import re

text = input().lower()
word = input().lower()
regex = fr'\b{word}\b'
match = re.findall(regex, text)
print(len(match))
