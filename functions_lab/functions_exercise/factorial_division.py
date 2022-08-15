def first_factorial(a):
    for x in range(1, a):
        a *= x
    return a


def second_factorial(b):
    for y in range(1, b):
        b *= y
    return b


number_one = int(input())
number_two = int(input())
first = first_factorial(number_one)
second = second_factorial(number_two)
print(f"{first / second:.2f}")
