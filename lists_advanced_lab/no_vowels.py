command = input()

vowels = ['a', 'o', 'u', 'e', 'i']
without_vowels = [x for x in command if x.lower() not in vowels]
print(''.join(without_vowels))
