employees = 3
questions_per_hour = 0
count = 0
for _ in range(employees):
    n = int(input())
    questions_per_hour += n

questions = int(input())

while True:
    if count % 4 == 0 and count != 0:
        count += 1
    if questions <= 0:
        break
    questions -= questions_per_hour
    count += 1

print(f"Time needed: {count}h.")
