import re

n = int(input())
regex = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
words = []
number = 0
for _ in range(n):
    text = input()
    messages = re.findall(regex, text)
    if messages:
        number = 0
        word = messages[0]
        first_word = word[0]
        second_word = word[1]
        for letter in second_word:
            number = str(ord(letter))
            words.append(number)
        print(f"{first_word}: {' '.join(words)}")
    else:
        print("The message is invalid")
