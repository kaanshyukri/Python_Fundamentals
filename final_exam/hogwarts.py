spell = input()

command = input()
while command != "Abracadabra":
    command = command.split()
    if command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command[0] == "Illusion":
        index, letter = command[1:]
        if int(index) > len(spell) - 1:
            print("The spell was too weak.")
        elif int(index) == len(spell):
            spell = spell[:int(index)] + letter
            print(spell)
        else:
            spell = spell[:int(index)] + letter + spell[int(index)+1:]
            print("Done!")
    elif command[0] == "Divination":
        first_substring, second_substring = command[1:]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif command[0] == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)
    else:
        print("The spell did not work!")
    command = input()
