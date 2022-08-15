number_of_heroes = int(input())
my_dict = {}
for _ in range(number_of_heroes):
    hero = input().split()
    hero_name, hp, mp = hero[0:]
    my_dict[hero_name] = {'HP': int(hp), 'MP': int(mp)}

text = input()
while text != "End":
    text_split = text.split(" - ")
    if text_split[0] == "CastSpell":
        hero_name, mp_needed, spell_name = text_split[1:]
        if my_dict[hero_name]['MP'] - int(mp_needed) < 0:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            my_dict[hero_name]['MP'] -= int(mp_needed)
            print(f"{hero_name} has successfully cast {spell_name} and now has {my_dict[hero_name]['MP']} MP!")
    elif text_split[0] == "TakeDamage":
        hero_name, damage, attacker = text_split[1:]
        if my_dict[hero_name]['HP'] - int(damage) > 0:
            my_dict[hero_name]['HP'] -= int(damage)
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {my_dict[hero_name]['HP']} HP left!")
        else:
            del my_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif text_split[0] == "Recharge":
        hero_name, amount = text_split[1:]
        if my_dict[hero_name]['MP'] + int(amount) > 200:
            print(f"{hero_name} recharged for {200 - my_dict[hero_name]['MP']} MP!")
            my_dict[hero_name]['MP'] = 200
        else:
            my_dict[hero_name]['MP'] += int(amount)
            print(f"{hero_name} recharged for {amount} MP!")
    elif text_split[0] == "Heal":
        hero_name, amount = text_split[1:]
        if my_dict[hero_name]['HP'] + int(amount) > 100:
            print(f"{hero_name} healed for {100 - my_dict[hero_name]['HP']} HP!")
            my_dict[hero_name]['HP'] = 100
        else:
            my_dict[hero_name]['HP'] += int(amount)
            print(f"{hero_name} healed for {amount} HP!")
    text = input()


for key, value in my_dict.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")



