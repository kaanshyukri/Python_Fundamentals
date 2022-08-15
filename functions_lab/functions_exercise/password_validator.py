text = input()
digits = 0
length_of_text = len(text)
all_num_chek = text.isalnum()
check = False
for c in text:
    if c.isdigit():
        digits += 1

if 6 <= length_of_text <= 10:
    check = True

if check and digits >= 2 and all_num_chek:
    print("Password is valid")
if not check:
    print("Password must be between 6 and 10 characters")
if not all_num_chek:
    print("Password must consist only of letters and digits")
if digits < 2:
    print("Password must have at least 2 digits")
