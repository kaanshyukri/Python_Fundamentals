function = input()
a = int(input())
b = int(input())


def calculation(text, number_one, number_two):
    result = 0

    if text == "multiply":
        result = number_one * number_two
    elif text == "divide":
        result = number_one // number_two
    elif text == "add":
        result = number_one + number_two
    elif text == "subtract":
        result = number_one - number_two

    return result


print(calculation(function, a, b))
