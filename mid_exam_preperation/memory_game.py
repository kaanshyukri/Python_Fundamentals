sequence = input().split()
command = input()
moves = 0
while command != "end":
    res = command.split()
    a = int(res[0])
    b = int(res[1])
    moves += 1
    if a == b or a < 0 or a >= (len(sequence)) or b < 0 or b >= (len(sequence)):
        result = len(sequence) // 2
        sequence.insert(int(result), (str(-moves) + "a"))
        sequence.insert(int(result), (str(-moves) + "a"))
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if sequence[a] != sequence[b]:
        print("Try again!")
        command = input()
        continue
    if sequence[a] == sequence[b]:
        removing = sequence.pop(a)
        sequence.remove(removing)
        print(f"Congrats! You have found matching elements - {removing}!")
    if len(sequence) == 0:
        break
    command = input()

if len(sequence) > 0:
    print("Sorry you lose :(")
    print(" ".join(sequence))
else:
    print(f"You have won in {moves} turns!")

