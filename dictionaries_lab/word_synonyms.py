number = int(input())
synonyms = {}
for i in range(number):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word] += [synonym]

for (key, value) in synonyms.items():
    print(f"{key} - {', '.join(value)}")



