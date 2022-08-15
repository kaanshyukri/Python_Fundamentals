number_one = int(input())
number_two = int(input())
text =  ""
for n in range(number_one, number_two + 1):
    text = chr(n)
    print(text, end=" ")
