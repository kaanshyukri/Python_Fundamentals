quantity = int(input())
days_left = int(input())
spirit = 0
money_spent = 0

for days in range(1, days_left+1):
    if days % 11 == 0:
        quantity +=2

    if days % 2 == 0:
        spirit += 5
        money_spent += quantity * 2
    if days % 3 == 0:
        spirit +=13
        money_spent += quantity*(5+3)
    if days % 5 == 0:
        spirit += 17
        money_spent += quantity*15
    if days % 10 == 0:
        spirit -=20
        money_spent += 23
        if days == days_left:
            spirit -=30
    if days % 15 == 0:
        spirit +=30


print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit}")

