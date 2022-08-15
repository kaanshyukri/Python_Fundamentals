tickets = [k.strip() for k in input().split(", ")]
symbols = ['@', '#', '$', '^']
condition = False
uninterrupted_one = False
uninterrupted_second = False
n_one = 0
n_two = 0
symbol = ""
for ticket in tickets:
    n_one = 0
    n_two = 0
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    first = ticket[0:10]
    second = ticket[10:]
    for s in symbols:
        if s in first and s in second:
            symbol = s
            condition = True
            continue
    if condition:
        for f in range(len(first)):
            if not first[f].isalpha():
                if not uninterrupted_one:
                    n_one += 1
            if 6 <= n_one <= 10 and f < 9:
                if first[f+1].isalpha():
                    uninterrupted_one = True
        for c in range(len(second)):
            if not second[c].isalpha():
                if not uninterrupted_second:
                    n_two += 1
            if 6 <= n_two <= 10 and c < 9:
                if second[c+1].isalpha():
                    uninterrupted_second = True
    if not condition:
        print(f'ticket "{ticket}" - no match')
    if n_one == n_two and condition and 6 <= n_one <= 10:
        if n_one == 10:
            print(f'ticket "{ticket}" - {n_one}{symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {n_one}{symbol}')
    if n_one > n_two and condition and 6 <= n_two <= 10:
        print(f'ticket "{ticket}" - {n_two}{symbol}')
    if n_one < n_two and condition and 6 <= n_one <= 10:
        print(f'ticket "{ticket}" - {n_one}{symbol}')


