info = input().split(" ")
team_a = 11
team_b = 11
players = []
condition = False
for card in info:
    if card not in players:
        players.append(card)
        if "A" in card:
            team_a -=1
        if "B" in card:
            team_b -=1
    if team_a < 7 or team_b < 7:
        condition = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if condition:
    print("Game was terminated")



