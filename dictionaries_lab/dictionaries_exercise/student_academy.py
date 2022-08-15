number = int(input())
students = {}
for _ in range(number):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

calc = 0
for key, value in students.items():
    for v in value:
        calc +=v
    res = calc / len(value)
    if res >= 4.50:
        print(f"{key} -> {res:.2f}")
    calc = 0



