def sum_numbers(first, second):
    return first + second


def subtract(x, y):
    return x - y


a = int(input())
b = int(input())
c = int(input())

add = sum_numbers(a, b)
sub = subtract(add, c)
print(sub)
