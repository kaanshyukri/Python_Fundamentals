employees_rate = list(map(int, input().split(" ")))
factor = int(input())

multiply_list = list(map(lambda x: x * factor, employees_rate))
filter_list = list(filter(lambda x: x >= (sum(multiply_list) / len(multiply_list)), multiply_list))

if len(filter_list) >= (len(multiply_list) / 2):
    print(f"Score: {len(filter_list)}/{len(multiply_list)}. Employees are happy!")
else:
    print(f"Score: {len(filter_list)}/{len(multiply_list)}. Employees are not happy!")



