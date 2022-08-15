version = input()

new_version = version.split(".")
first_number = int(new_version[0])
second_number = int(new_version[1])
third = int(new_version[2])

if third + 1 == 10:
    third = 0
    second_number += 1
    if second_number == 10:
        second_number = 0
        first_number += 1
elif third + 1 < 10:
    third += 1
print(f"{first_number}.{second_number}.{third}")
