def iseven(x):
    return x % 2 == 0


numbers = input().split(" ")
number_as_digits = []

for n in numbers:
    number_as_digits.append(int(n))


number_list = list(filter(iseven, number_as_digits))

print(number_list)
