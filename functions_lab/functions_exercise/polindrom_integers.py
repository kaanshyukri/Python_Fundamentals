def palindrome():
    for x in num_list:
        if x[0] == x[-1]:
            print("True")
        else:
            print("False")


nums = input().split(", ")
num_list = []

for n in nums:
    num_list.append(n)


palindrome()
