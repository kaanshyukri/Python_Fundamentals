command = input().split(" ")
number = []

for i in command:
    number.append(int(i))

print(f"The minimum number is {min(number)}")
print(f"The maximum number is {max(number)}")
print(f"The sum number is: {sum(number)}")
