number = int(input())
word = input()
first_list = []
second_list = []
for _ in range(number):
    current_word = input()
    first_list.append(current_word)
    if word in current_word:
        second_list.append(current_word)
print(first_list)
print(second_list)
