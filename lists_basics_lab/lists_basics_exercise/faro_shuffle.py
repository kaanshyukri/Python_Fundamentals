card = input().split(' ')
shuffles = int(input())
reordered = []

a = int((len(card)) / 2)

for n in range(shuffles):

    for i in range(a):
        reordered.append(card[i])
        b = int(a + i)
        reordered.append(card[b])

    card.clear()
    card.extend(reordered)
    reordered.clear()

print(card)