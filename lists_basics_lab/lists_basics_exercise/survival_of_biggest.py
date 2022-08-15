numbers = input().split(" ")
count = int(input())
list_numbers = list(map(int,numbers))

list_numbers.sort()

for _ in range(count):
    remove_this = list_numbers[0]
    list_numbers.remove(remove_this)
    numbers.remove(str(remove_this))

list_numbers.reverse()

print(", ".join(numbers))









