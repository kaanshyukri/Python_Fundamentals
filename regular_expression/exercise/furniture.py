import re

command = input()
regex = r'([A-Za-z]+)<<(\d+\.?\d+)!(\d+)'
total = 0
my_list = []
while command != "Purchase":
    match = re.search(regex, command)
    if match:
        furniture, price, quantity = match.groups()
        my_list.append(furniture)
        total += float(price) * int(quantity)
    command = input()


print('Bought furniture:')
for my in my_list:
    print(my)
print(f'Total money spend: {total:.2f}')
