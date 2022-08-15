import re

text = input()
regex = r"(=|\/)[A-Z][A-Za-z]{2,}(\1)"
destination = re.finditer(regex, text)
destination_list = []
travel_points = 0
valid = ''
print_list = []

for country in destination:
    destination_list.append(country.group())
for country in destination_list:
    replaced = country.replace(country[0],'')
    travel_points += len(replaced)
    print_list.append(replaced)

print(f"Destinations: {', '.join(print_list)}")
print(f"Travel Points: {travel_points}")
