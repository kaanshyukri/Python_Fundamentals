command = input()
total = 0
taxes = 0
while command != "special" or command != "regular":
    command = float(command)
    total += command
    if command < 0:
        print("Invalid price!")
        command = input()
        continue
    command = input()

if command == "special":
    taxes = total * 0.20

if total == 0:
    print("Invalid order")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total:.2f}$\n"
          f"Taxes: {taxes:.2f}\n"
          f"-----------\n"
          f"Total price: {(total + taxes):.2f}")

