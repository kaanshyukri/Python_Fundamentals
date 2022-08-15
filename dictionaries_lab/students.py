command = input()
students = {}

while ":" in command:

    res = command.split(":")
    name = res[0]
    number = int(res[1])
    course = res[2]
    if course not in students:
        students[course] = {}

    students[course][name] = number
    command = input()
course_command = " ".join(command.split("_"))
for (key, value) in students[course_command].items():
    print(f"{key} - {value}")