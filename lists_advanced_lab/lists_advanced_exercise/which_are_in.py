first_command = input().split(", ")
second_command = input().split(", ")
string_list = []

for i in first_command:
    for x in second_command:
        if i in x:
            if i not in string_list:
                string_list.append(i)

print(string_list)
