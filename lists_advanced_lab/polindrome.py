words = input().split(" ")
palindrome_word = input()
times = 0

palindrome_list = [x for x in words if x == x[::-1]]
palindrome_count = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")

