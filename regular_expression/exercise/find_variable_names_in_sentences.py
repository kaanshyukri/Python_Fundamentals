import re

command = input()
regex = r'\b_([A-Za-z0-9]+)\b'
match = re.findall(regex, command)
if match:
    print(','.join(match))
