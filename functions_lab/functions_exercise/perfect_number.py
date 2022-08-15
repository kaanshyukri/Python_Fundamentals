def find_number():
    perfect_number = 0
    for x in range(1, number):
        if number % x == 0:
            perfect_number += x

    if perfect_number == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(find_number())
