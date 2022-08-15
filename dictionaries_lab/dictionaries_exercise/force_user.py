command = input()
forces = {}
condition = False
values = []
keys = []
x_list = []
y_list = []
while command != "Lumpawaroo":
    condition = False
    force_user = ''
    side = ''
    if "|" in command:
        command = command.split(" | ")
        force_user = command[1]
        side = command[0]
        for x, y in forces.items():
            x_list.append(x)
            y_list.append(y)
        if forces:
            if side not in x_list or side not in forces:
                forces[side] = []
            if force_user not in y_list or side not in forces:
                forces[side].append(force_user)
        x_list.clear()
        y_list.clear()

    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        side = command[1]
        for key, value in forces.items():
            keys.append(key)
            for v in value:
                values.append(v)
                if force_user == v:
                    forces[key].remove(v)
                    condition = True
                    if condition:
                        forces[side].append(force_user)
                        print(f"{force_user} joins the {side} side!")
                        continue
        if force_user not in values:
            if side not in keys:
                forces[side] = []
            forces[side].append(force_user)
            print(f"{force_user} joins the {side} side!")
    values.clear()
    keys.clear()
    command = input()

for k, v in forces.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
    for s in v:
        print(f"! {s}")

