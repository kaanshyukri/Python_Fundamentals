num = int(input())
first_list = []
second_list = []
for _ in range(num):
    number = int(input())
    first_list.append(number)

word = input()
i = 0

while i < num:
    if word == "even":
        if first_list[i] % 2 == 0:
            second_list.append(first_list[i])
    elif word == "odd":
        if first_list[i] % 2 != 0:
            second_list.append(first_list[i])
    elif word == "negative":
        if first_list[i] < 0:
            second_list.append(first_list[i])
    elif word == "positive":
        if first_list[i] >= 0:
            second_list.append(first_list[i])
    i += 1

print(second_list)




