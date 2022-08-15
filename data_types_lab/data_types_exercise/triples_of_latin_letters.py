number = int(input())

for first in range(97, 97 + number):
    line_one = chr(first)
    for second in range (97, 97 + number):
        line_two = chr(second)
        for third in range(97, 97 + number):
            line_three = chr(third)
            print(f"{line_one}{line_two}{line_three}")
