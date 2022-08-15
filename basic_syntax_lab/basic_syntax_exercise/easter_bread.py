budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_for_bread_price = (1.25 * flour_price) / 4
breads_made = 0
eggs = 0
money_spent = 0
while budget - money_spent > 0:
    if budget < money_spent + (eggs_price + flour_price + milk_for_bread_price):
        break
    else:
        breads_made += 1
        money_spent += (eggs_price + flour_price + milk_for_bread_price)
        eggs += 3
        if breads_made % 3 == 0:
            eggs -= (breads_made - 2)

print(
    f"You made {breads_made} loaves of Easter bread! Now you have {eggs} eggs and {(budget - money_spent):.2f}BGN left.")






