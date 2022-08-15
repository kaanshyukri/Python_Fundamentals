import re
command = input()
domains = []
reg = r'((www\.)([A-Za-z0-9-]+[-[A-Za-z0-9-]+)(\.[a-z]+)+)'
while command:
    match = re.search(reg, command)
    if match:
        domains.append(match.group(1))
    command = input()

if domains:
    for domain in domains:
        print(domain)
