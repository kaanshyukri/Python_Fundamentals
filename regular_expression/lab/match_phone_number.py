import re
phones = input()
regex = r'\+359 [2] [0-9]{3} [0-9]{4}|\+359-[2]-[0-9]{3}-[0-9]{4}\b'
res = re.findall(regex, phones)
print(', '.join(res))