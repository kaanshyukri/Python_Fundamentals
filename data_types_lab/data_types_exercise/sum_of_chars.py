number = int(input())
sum = 0
for n in range(1, number + 1):
    line = input()
    sum += ord(line)

print(f"The sum equals: {sum}")