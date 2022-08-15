word_one = input()
word_two = input()
word_three = input()

my_list = [word_one, word_two, word_three]
my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)
