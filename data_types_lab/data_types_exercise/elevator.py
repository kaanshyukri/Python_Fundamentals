number_of_people = int(input())
capacity = int(input())
sum = number_of_people / capacity
if sum == 0:
    print(f"{int(number_of_people // capacity)}")
elif 0 < number_of_people % capacity <= capacity:
    print(f"{int((sum) + 1)} ")
else:
    print(f"{int(sum)}")

