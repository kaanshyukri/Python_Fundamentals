type_of_fire = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0

print("Cells:")
for fire in type_of_fire:
    current_fire = fire.split(" = ")
    first = current_fire[0]
    second = int(current_fire[1])
    if total_fire + second > water_amount:
        continue
    if first == "High":
        if 81 <= second <= 125:
            effort += (second * 0.25)
            total_fire += second
            print(f" - {second}")
    elif first == "Medium":
        if 51 <= second <= 80:
            effort += (second * 0.25)
            total_fire += second
            print(f" - {second}")
    elif first == "Low":
        if 1 <= second <= 50:
            effort += (second * 0.25)
            total_fire += second
            print(f" - {second}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




