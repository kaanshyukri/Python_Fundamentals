command = input()
to_do_list = [""] * 11

while command != "End":
    res = command.split("-")
    importance = int(res[0])
    note = res[1]
    to_do_list[importance] = note
    command = input()

removing = [x for x in to_do_list if x != ""]
print(removing)
