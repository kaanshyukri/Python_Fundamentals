word = input()

text = input()
while text != "Done":
    command = text.split()
    if command[0] == "TakeOdd":
        if " " not in word:
            word += " "
        for index in range(1, len(word), 2):
            word += word[index]
        word = word.split()
        word = word[1]
        print(word)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        word = word[:index] + word[index+length:]
        print(word)
    elif command[0] == "Substitute":
        substring, substitute = command[1:]
        if substring in word:
            word = word.replace(substring, substitute)
            print(word)
        else:
            print("Nothing to replace!")
    text = input()

print(f"Your password is: {word}")
