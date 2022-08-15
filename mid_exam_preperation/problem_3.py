numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)
new_list = []

for n in numbers:
    if n > average:
        new_list.append(n)
new_list.sort(reverse=True)
if len(new_list) > 5:
    res = len(new_list) - 5
    for _ in range(res):
        new_list.pop()

if len(new_list) > 0:
    new_list = [str(x) for x in new_list]
    print(" ".join(new_list))
else:
    print("No")
