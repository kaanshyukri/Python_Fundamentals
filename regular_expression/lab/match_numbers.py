import re

numbers = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
res = re.finditer(regex, numbers)
for r in res:
    print(r.group(), end=' ')
dsdsddsd