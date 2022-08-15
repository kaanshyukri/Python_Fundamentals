words = input().split()
res = ""
for word in words:
    w = word * len(word)
    res += w

print(res)
