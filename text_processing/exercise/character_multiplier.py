strings = input().split()
first = strings[0]
second = strings[1]
diff = abs(len(first) - len(second))
total = 0
n = 0
if len(first) > (len(second)):
    for index in range(0, len(first) - diff):
        total += ord(first[index]) * ord((second[index]))
        n += 1
    for x in range(n, len(first)):
        total += ord(first[x])
elif len(second) > len(first):
    for index in range(0, len(second) - diff):
        total += ord(first[index]) * ord((second[index]))
        n += 1
    for x in range(n, len(second)):
        total += ord(second[x])
else:
    for index in range(0, len(first)):
        total += ord(first[index]) * ord((second[index]))
print(total)
