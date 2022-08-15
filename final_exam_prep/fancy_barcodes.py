import re

n = int(input())
regex = r"((@#{1,})[A-Z][A-Za-z0-9]{4,}[A-Z](@#{1,}))"
number_text = ''

for _ in range(n):
    text = input()
    word = re.findall(regex, text)
    if word:
        number_text = ''
        val = word[0]
        valid = val[0]
        for v in valid:
            if v.isdigit():
                number_text += v
        if number_text:
            print(f"Product group: {number_text}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
