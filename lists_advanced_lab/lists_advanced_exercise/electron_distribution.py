number = int(input())
numbers_list = []

for n in range(1, number+1):
    res = 2 * (n ** 2)
    if sum(numbers_list) + res >= number:
        subtract = number - sum(numbers_list)
        numbers_list.append(subtract)
        break
    if res < number:
        res = 2*(n**2)
        numbers_list.append(res)
    if sum(numbers_list) >= number:
        break

print(numbers_list)
