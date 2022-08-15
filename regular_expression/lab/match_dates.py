import re
dates = input()
regex = r'(\d{2})(\.|-|\/)([A-Z][a-z]{2})(\2)(\d{4})'
res = re.finditer(regex, dates)

for r in res:
    print(f"Day: {r[1]}, Month: {r[3]}, Year: {r[5]}")
