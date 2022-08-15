number = int(input())
sum = 0

for n in range(1, number + 1):
    litres = int(input())
    sum += litres
    if sum > 255:
        print("Insufficient capacity!")
        sum -= litres
    if n == number:
        break

print(sum)

