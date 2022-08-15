commands = input().split()
my_dict = {}
my_list = []
for word in commands:
    w = word.lower()
    if w not in my_dict:
        my_dict[w] = 1
    elif w in my_dict:
        my_dict[w] += 1
    
for (key, value) in my_dict.items():
    if value % 2 != 0:
        my_list.append(key)

print(' '.join(my_list))