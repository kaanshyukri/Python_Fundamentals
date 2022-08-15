numbers = list(map(int, input(). split(", ")))
group = 10
res = max(numbers) // 10

for x in range(res + 1):
    numbers_list = [y for y in numbers if y <= group]
    print(f"Group of {group}'s: {numbers_list}")
    group += 10
    for c in numbers_list:
        numbers.remove(c)
    if not numbers:
        break
