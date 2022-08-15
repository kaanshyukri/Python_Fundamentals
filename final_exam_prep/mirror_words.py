import re

text = input()
regex = r'(@|#)([A-Za-z]{3,})(\1){2}([A-Za-z]{3,})(\1)'
words = re.finditer(regex, text)
valid_words, mirror_words = [], []

for word in words:
    first_word, second_word = word.group(2), word.group(4)
    valid_words.append(first_word)
    if first_word == second_word[::-1]:
        mirror_words.append(first_word)
        mirror_words.append(second_word)

if valid_words:
    print(f"{len(valid_words)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    for index in range(0, len(mirror_words), 2):
        if index == len(mirror_words) - 2:
            print(f"{mirror_words[index]} <=> {mirror_words[index+1]}")
        else:
            print(f"{mirror_words[index]} <=> {mirror_words[index+1]}", end=', ')
else:
    print("No mirror words!")

