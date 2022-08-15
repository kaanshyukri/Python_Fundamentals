import re
from math import floor
text = input()
regex = r'(#|\|)(([A-Z][a-z]+)( [A-Z][a-z]+)*)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)'
food = re.finditer(regex, text)
calories = 0
foods, dates, cal = [], [], []

for item in food:
    foods.append(item.group(2))
    dates.append(item.group(6))
    cal.append(int(item.group(8)))

days = floor(sum(cal) / 2000)
print(f"You have food to last you for: {days} days!")
for index in range(len(foods)):
    print(f"Item: {foods[index]}, Best before: {dates[index]}, Nutrition: {cal[index]}")

