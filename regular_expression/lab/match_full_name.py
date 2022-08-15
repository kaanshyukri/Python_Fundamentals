import re

text = input()
res = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
final = re.findall(res, text)
print(" ".join(final))