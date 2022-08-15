ban_words = input().split(", ")
text = input()

for ban in ban_words:
    if ban in text:
        text = text.replace(ban, "*" * len(ban))

print(text)