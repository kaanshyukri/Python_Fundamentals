food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000
condition = True
for days in range(1, 31):
    food -= 300
    if days % 2 == 0:
        res = food * 0.05
        hay -= res
    if days % 3 == 0:
        res_two = (1/3) * pig_weight
        cover -= res_two
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        condition = False
        break

if condition:
    print(f"Everything is fine! Puppy is happy! Food: {(food / 1000):.2f}, Hay: {(hay / 1000):.2f},"
          f" Cover: {(cover / 1000):.2f}.")
