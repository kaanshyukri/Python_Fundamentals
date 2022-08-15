food = input().split(" ")
food_list = [x for x in food if len(x) % 2 == 0]
print("\n".join(food_list))
