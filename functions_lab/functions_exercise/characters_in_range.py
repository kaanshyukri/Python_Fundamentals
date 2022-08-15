def strings(a, b):
    for letter in range(ord(a) + 1, ord(b)):
        ascii_list.append(chr(letter))
    return ascii_list


string_a = input()
string_b = input()
ascii_list = []

print(" ".join(strings(string_a, string_b)))