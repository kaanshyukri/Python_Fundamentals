import re

texts = input().split()
total = 0
my_dict = {}
final = 0
for text in texts:
    res = re.split('(\d+)', text)
    first = res[0]
    number = int(res[1])
    second = res[2]
    for i in range(0, 2):
        if i == 0:
            if first.isupper():
                first = first.lower()
                total = number / int(ord(first) - 96)
            elif not first.isupper():
                total = number * int(ord(first) - 96)
        elif i == 1:
            if second.isupper():
                second = second.lower()
                total = (total - int(ord(second) - 96))
            elif not first.isupper():
                total = total + int(ord(second) - 96)
    if text not in my_dict:
        my_dict[text] = 0
    my_dict[text] += total
for value in my_dict.values():
    final += value
print(f"{final:.2f}")
