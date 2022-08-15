sequence = list(map(int, input().split()))
target = input()
count = 0
while target != "End":
    target = int(target)
    if 0 <= target < len(sequence):
        if sequence[target] != -1:
            value = sequence[target]
            sequence[target] = -1
            count += 1
            for i in range(len(sequence)):
                if sequence[i] == -1:
                    continue
                if value < sequence[i]:
                    sequence[i] -= value
                elif value >= sequence[i]:
                    sequence[i] += value
    target = input()
sequence = [str(x) for x in sequence]
without = " ".join(sequence)
print(f"Shot targets: {count} -> {without}")
