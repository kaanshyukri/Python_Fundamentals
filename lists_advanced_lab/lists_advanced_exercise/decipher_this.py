import re

words = input().split(" ")
words_list = []
for word in words:
    res = re.split('(\d+)', word)
    number = chr(int(res[1]))
    strings = res[2]
    if len(strings) <= 1:
        words_list.append(f"{number}{strings[-1]}{strings[1:(len(strings) - 1)]}")
    else:
        words_list.append(f"{number}{strings[-1]}{strings[1:(len(strings) - 1)]}{strings[0]}")


print(' '.join(words_list))
