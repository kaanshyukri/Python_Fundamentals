ban = input()
word = input()

while ban in word:
    word = word.replace(ban, "")

print(word)