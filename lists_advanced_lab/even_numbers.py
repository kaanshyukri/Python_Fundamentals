numbers = input().split(", ")
numbers_int = list(map(int, numbers))
found_indices = list(map(lambda x: x if numbers_int[x] % 2 == 0 else 'no', range(len(numbers))))
even_indices = [x for x in found_indices if x != 'no']
print(even_indices)

