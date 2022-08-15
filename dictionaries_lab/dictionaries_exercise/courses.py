command = input()
courses = {}

while command != "end":
    res = command.split(" : ")
    course_name = res[0]
    student_name = res[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()


for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for s in value:
        print(f"-- {s}")
