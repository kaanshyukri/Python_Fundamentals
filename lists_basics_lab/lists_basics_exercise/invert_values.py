n = input().split(" ")
numbers = []
for num in n:
    num = int(num)
    if num > 0:
        numbers.append(-int(num))
    elif num <= 0:
        numbers.append(abs(num))

print(numbers)