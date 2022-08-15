amount_of_experience = float(input())
battles = int(input())
gained = 0
condition = False
count = 0
for battle in range(1, battles + 1):
    gain = float(input())
    count += 1
    gained += gain
    if battle % 3 == 0 and battle % 15 != 0:
        gained += (gain * 0.15)
    if battle % 5 == 0 and battle % 15 != 0:
        gained -= (gain * 0.10)
    if battle % 15 == 0:
        gained += (gain * 0.05)
    if gained >= amount_of_experience:
        condition = True
        break


if condition:
    print(f"Player successfully collected his needed experience for {count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(amount_of_experience - gained):.2f} more needed.")