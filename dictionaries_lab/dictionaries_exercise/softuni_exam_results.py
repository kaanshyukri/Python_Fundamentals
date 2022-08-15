command = input()
exam = {}
language_dict = {}
while command != "exam finished":
    command = command.split("-")
    name = command[0]
    language = command[1]
    if language == "banned":
        del exam[name]
        command = input()
        continue
    points = int(command[2])
    if name in exam:
        if exam[name] < points:
            exam[name] = points
    else:
        exam[name] = points

    if language not in language_dict:
        language_dict[language] = 0
    language_dict[language] += 1
    command = input()
print("Results:")
for k, v in exam.items():
    print(f"{k} | {v}")
print("Submissions:")
for x, y in language_dict.items():
    print(f"{x} - {y}")

