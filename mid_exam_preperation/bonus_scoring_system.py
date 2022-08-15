students = int(input())
lectures = int(input())
bonus = int(input())
max_number = 0
total_bonus = 0
for _ in range(students):
    attendance = int(input())
    if max_number < attendance:
        max_number = attendance
if students > 0:
    total_bonus = (max_number / lectures) * (5 + bonus)
print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_number} lectures.")
