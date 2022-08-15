import re

command = input()
regex = r'\d+'
while command:
    match = re.findall(regex, command)
    if match:
        for m in match:
            print(m, end=' ')
    command = input()
