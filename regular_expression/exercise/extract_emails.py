import re

text = input()
regex = r'((?<= )([a-z0-9]+[-\.\_a-z0-9]*)@([a-z]+)(-[a-z]+)*\.([a-z\.]+))\b'
match = re.findall(regex, text)
if match:
    for m in match:
        print(m[0])



