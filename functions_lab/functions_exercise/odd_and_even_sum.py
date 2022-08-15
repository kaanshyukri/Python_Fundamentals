def sum_of_sum(string_number):
    odd_sum = 0
    even_sum = 0
    for n in string_number:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
sum_of_sum(number)
