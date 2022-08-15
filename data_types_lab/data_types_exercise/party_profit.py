group_size = int(input())
days = int(input())
coins = 0

for days_to in range(1, days + 1):
    if days_to % 15 == 0:
       group_size += 5
    if days_to % 10 == 0:
        group_size -= 2
    coins += (50 - (group_size * 2))
    if days_to % 3 == 0:
        coins -= (group_size * 3)
    if days_to % 5 == 0:
        coins += (group_size * 20)
        if days_to % 3 == 0:
            coins -= (group_size * 2)

coins_per_companion = int(coins / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")






