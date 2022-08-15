text = input()
nums = []
alpha = []
symbols = []

for s in text:
    if s.isdigit():
        nums.append(s)
    elif s.isalpha():
        alpha.append(s)
    else:
        symbols.append(s)

print("".join(nums))
print("".join(alpha))
print("".join(symbols))
